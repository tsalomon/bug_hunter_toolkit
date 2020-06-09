# The sendingRequest and responseReceived functions will be called for all
# requests/responses sent/received by ZAP, including automated tools (e.g.
# active scanner, fuzzer, ...)

# 'initiator' is the component the initiated the request:
#      1   PROXY_INITIATOR
#      2   ACTIVE_SCANNER_INITIATOR
#      3   SPIDER_INITIATOR
#      4   FUZZER_INITIATOR
#      5   AUTHENTICATION_INITIATOR
#      6   MANUAL_REQUEST_INITIATOR
#      7   CHECK_FOR_UPDATES_INITIATOR
#      8   BEAN_SHELL_INITIATOR
#      9   ACCESS_CONTROL_SCANNER_INITIATOR
#     10   AJAX_SPIDER_INITIATOR

# For the latest list of values see the HttpSender class:
# https://github.com/zaproxy/zaproxy/blob/master/src/org/parosproxy/paros/network/HttpSender.java
# 'helper' just has one method at the moment: helper.getHttpSender() which
# returns the HttpSender instance used to send the request.
#
# New requests can be made like this:
# msg2 = msg.cloneAll() # msg2 can then be safely changed without affecting msg
# helper.getHttpSender().sendAndReceive(msg2, false)
# print('msg2 response code =' + msg2.getResponseHeader().getStatusCode())

HANDLE = "test"
EMAIL = "<username>+x@wearehackerone.com"
SITE = "HackerOne"
HEADER = "X-Bug-Bounty"
SHA256_FLAG = "9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A08" #SHA256(test)
EVENT_ID = "T1-123"
TOOL_NAME = "ZAP"
TOOL_VERSION = "2.9.0"

header = {	"USERNAME": "".join([SITE, "-", HANDLE]), \
			"EMAIL": "".join(["ID", "-", EMAIL]), \
			"UID": "".join(["ID", "-", SHA256_FLAG]), \
			"TOOLVV": "".join([TOOL_NAME, "-version-", TOOL_VERSION]), \
			"TOOL":TOOL_NAME }

def sendingRequest(msg, initiator, helper):

	# Most common configuration
	msg.getRequestHeader().setHeader(HEADER, header["USERNAME"]); 
	msg.getRequestHeader().setHeader(HEADER, header["TOOLVV"]); 

	msg.getRequestHeader().setHeader(HEADER, header["EMAIL"]); 
	msg.getRequestHeader().setHeader(HEADER, header["UID"]);
	msg.getRequestHeader().setHeader(HEADER, header["TOOL"]); 

	# Debugging can be done using print like this
    	print('sendingRequest called with headers =' + msg.getRequestHeader().getHeadersAsString())

def responseReceived(msg, initiator, helper):
	# Debugging can be done using print like this
	print('responseReceived called for url=' +
	msg.getRequestHeader().getURI().toString())
