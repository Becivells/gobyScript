#!/usr/bin/env python3

import os
import sys
import glob
import shutil
import argparse
import subprocess


def run_CMD(cmdlist):
    p = subprocess.Popen(cmdlist, shell=False, universal_newlines=True)
    p.communicate()
    if p.returncode != 0:
        sys.exit(p.returncode)

def lint_check(args):
    if shutil.which("golangci-lint"):
        print("[+] check template %s style"%args.template)

        lintcmd = ["golangci-lint","run",args.template,
                   "--disable-all",
                   "--enable",
                   "asciicheck"
                   ",dogsled"
                   ",dupl"
                   ",gofumpt"
                   ",goheader"
                   ",goimports"
                   ",gofmt"
                   ",ifshort"
                   ",whitespace"
                   ",wsl"
                   ]
        print("[+][lint] cmd: %s" % " ".join(lintcmd))
        run_CMD(lintcmd)
    else:
        print("[-] please install golangci-lint we need check")

def gofmt(args):
    if shutil.which("gofmt"):
        print("[+] gofmt template %s" % args.template)
        fmtcmd = ["gofmt", '-s', '-w', args.template]
        print("[+][gofmt] cmd: %s" % " ".join(fmtcmd))
        p = subprocess.Popen(fmtcmd, shell=False, universal_newlines=True)
        p.wait()
    else:
        print("[-] please install golang we need gofmt")


def gen_POC(args):
    if args.genpoc:
        if os.environ.get("goby_proxy"):
            args.proxy = os.environ.get("goby_proxy")
        if not args.cveid or not args.exportFile:
            print("cve or exportFile not none")
            sys.exit(1)

        cmd = [
            "goby-cmd",
            "-mode", "genpoc",
            "-CVEID", args.cveid,
            "-exportFile", args.exportFile
        ]
        if args.proxy:
            cmd.append("-proxy")
            cmd.append(args.proxy)
        if not args.test:
            print("[+][genpoc] cmd: %s" % " ".join(cmd))
            run_CMD(cmd)
        else:
            print("[+][genpoc] cmd: %s" % " ".join(cmd))
        sys.exit(0)


def run_POCEXP(args):
    cmd = [
        "goby-cmd",
        "-mode", "runpoc",
        "-target", args.url,
        "-pocFile", args.template,
        "-params", args.params,
    ]

    if args.godserver != "https://gobygo.net":
        cmd.append("-godserver")
        cmd.append(args.godserver)

    mode = "poc"
    if args.poc:
        cmd.append("-operation")
        cmd.append("scan")
    else:
        mode = "exp"
        cmd.append("-operation")
        cmd.append("exploit")

    if not args.test:
        print("[+][%s] cmd: %s" % (mode," ".join(cmd)))
        run_CMD(cmd)
    else:
        print("[+][%s] cmd: %s" % (mode," ".join(cmd)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='goby-cmd poc fast test '
                                                 'you can set env '
                                                 'export goby_params=\'{"cmd":"whoami"}\' '
                                                 'or '
                                                 'export goby_proxy="http://127.0.0.1:8080"')

    genpoc = parser.add_argument_group("genpoc","genpoc template from cveid")
    pocexp = parser.add_argument_group("poc/exp","test poc or exp")
    group=pocexp.add_mutually_exclusive_group()
    parser.add_argument("--nolint",action='store_true',help="golangci-lint check default true")
    parser.add_argument("--nofmt", action='store_true', help="golangci-lint check default true")
    group.add_argument("--poc", action='store_true', help="poc mode")
    group.add_argument("--exp", action='store_true', help="exp mode")
    pocexp.add_argument("--test", action='store_true', help="only print command and not execute")
    pocexp.add_argument("-u", "--url", type=str,  help="test target")
    pocexp.add_argument("-t", "--template", type=str, help="goby exp template")
    pocexp.add_argument("-d", "--godserver", default='https://gobygo.net', help="default https://gobygo.net")
    pocexp.add_argument("-p", "--params", default='{"cmd":"whoami"}', help="default '{\"cmd\":\"whoami\"}' ")
    genpoc.add_argument("-g", "--genpoc", action='store_true', help="genpoc")
    genpoc.add_argument("-c", "--cveid", type=str, help="test url")
    genpoc.add_argument("-e", "--exportFile", type=str, help="test url")
    genpoc.add_argument("--proxy", default="", help="proxy with cve search default  None")
    args = parser.parse_args()

    gen_POC(args)

    if not args.template:
        tfile = glob.glob("*.go")
        if len(tfile) == 1:
            args.template = tfile[0]
            print("[+] use templates %s" % (args.template))
        elif len(tfile) >= 1:
            print("[-] templates more than one,please use -t/--templates")
        else:
            print("[-] not find template please change dir or use: -t/--templates")
            sys.exit(1)
    if not os.path.exists(args.template):
        print(args.template)
        print("[-] args templates path not find")
        sys.exit(1)

    if not args.nofmt:
        gofmt(args)

    if not args.nolint:
        lint_check(args)

    if not args.url:
        with open(args.template, 'r') as f:
            lines = f.read().strip().split("\n")
            lastline = lines[-1].strip()
            if lastline.startswith("//"):
                args.url = lastline.lstrip("/").strip()
                print("[+] use target %s from template %s" % (args.url,args.template))

    if not args.url:
        print("the following arguments are required: -u/--url")
        sys.exit(-1)

    if os.environ.get("goby_params"):
        args.params =os.environ.get("goby_params")

    if os.environ.get("godserver"):
        args.godserver =os.environ.get("godserver")

    if not args.poc and not args.exp:
        print("[-] the following arguments are required: --poc/--exp ")
        sys.exit(1)

    run_POCEXP(args)



