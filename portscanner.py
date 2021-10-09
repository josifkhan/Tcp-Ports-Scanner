


# Coded By Josif
# Contact : https://facebook.com/josifkhangg
# More tools : https://github.com/josifkhan
# 

import base64, codecs
magic = 'aW1wb3J0IGJhc2U2NCwgY29kZWNzCm1hZ2ljID0gJ0Nnb2phbVJyWkd0a2EyUnJaV3RsYTJWbGEydGxhMlZyWldWclpXdGxhMnRsYTJWbGEydGxhM2RyZDNkcmQzZDNhMnQzZDJ0cmQydDNhM2QzYTNkdGQyMXRkMjEzYlhkM2JYZHRiWGQzYlcxM2JYZDNiVzEzYlhkdGQzZHRiWGR0ZDIxM2JYZHRkMjEzYTNkdGQydDNhM2R0Wld0bGEyVmxiVzEzQ2dwcGJYQnZjblFnYzI5amEyVjBMSE41Y3dwcGJYQnZjblFnZEdsdFpTeHZjd3BtY205dElHUmhkR1YwYVcxbElHbHRjRzl5ZENCa1lYUmxkR2x0WlFvS2RISjVPZ29nSUNBZ1puSnZiU0IwWlhKdFkyOXNiM0lnYVcxd2IzSjBJR052Ykc5eVpXUUtJQ0FnSUdSbFppQmpiMlJsWkNncE9nb2dJQ0FnSUNBZ0lHOXpMbk41YzNSbGJTZ25ZMnhsWVhJbktRb2dJQ0FnSUNBZ0lIQTlJa052WkdWa0lFSjVJRXB2YzJsbUlnb2dJQ0FnSUNBZ0lHWnZjaUJwYVNCcGJpQndPZ29nSUNBZ0lDQWdJQ0FnSUNCbWIzSWdhU0JwYmlCcGFUb0tJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lIUnBiV1V1YzJ4bFpYQW9NQzR4S1FvZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnY0hKcGJuUW9hU3hsYm1ROUp5Y3BDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQnplWE11YzNSa2IzVjBMbVpzZFhOb0tDa0tJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDTjBhVzFsTG5Oc1pXVndLREVwQ2lBZ0lDQWdJQ0FnZEdsdFpTNXpiR1ZsY0NneEtRb2dJQ0FnZEdsdFpTNXpiR1ZsY0NneEtRb2dJQ0FnQ2lBZ0lDQmtaV1lnYzJOaGJtNWxjbkJ2Y25Rb0tUb0tJQ0FnSUNBZ0lDQUtJQ0FnSUNBZ0lDQmpiMlJsWkNncENpQWdJQ0FnSUNBZ2IzTXVjM2x6ZEdWdEtDZGpiR1ZoY2ljcENpQWdJQ0FnSUNBZ2RISjVPZ29nSUNBZ0lDQWdJQ0FnSUNCd2J6MWJKekl3Snl3Z0p6SXhKeXdnSnpJeUp5d2dKekl6Snl3Z0p6STFKeXdnSnpVd0p5d2dKelV4Snl3Z0p6VXpKeXdnSnpZM0p5d2dKelk0Snl3Z0p6WTVKeXdnSnpnd0p5d2dKekV4TUNjc0lDY3hNVGtuTENBbk1USXpKeXdnSnpFek5TY3NJQ2N4TXpZbkxDQW5NVE0zSnl3Z0p6RXpPQ2NzSUNjeE16a25MQ0FuTVRRekp5d2dKekUyTVNjc0lDY3hOakluTENBbk16ZzVKeXdnSnpRME15Y3NJQ2M1T0RrbkxDQW5PVGt3Snl3Z0p6TXpPRGtuTENBbk1UY25MQ0FuTVRnbkxDQW5NalluTENBbk5ERW5MQ0FuTkRJbkxDQW5ORGtuTENBbk5UY25MQ0FuTnpBbkxDQW5OemtuTENBbk9ERW5MQ0FuT0RJbkxDQW5PRGduTENBbk1UQXhKeXdnSnpFd01pY3NJQ2N4TURjbkxDQW5NVEE1Snl3Z0p6RXhNU2NzSUNjeE1UTW5MQ0FuTVRFMUp5d2dKekV4Tnljc0lDY3hNVGduTENBbk1UVXlKeXdnSnpFMU15Y3NJQ2N4TlRZbkxDQW5NVFUzSnl3Z0p6RTFPQ2NzSUNjeE5Ua25MQ0FuTVRZd0p5d2dKekUzTUNjc0lDY3hOemtuTENBbk1Ua3dKeXdnSnpFNU1TY3NJQ2N4T1RJbkxDQW5NVGswSnl3Z0p6SXdNU2NzSUNjeU1Ea25MQ0FuTWpFekp5d2dKekl4T0Njc0lDY3lNakFuTENBbk1qVTVKeXdnSnpJMk5DY3NJQ2N6TVRFbkxDQW5NekU0Snl3Z0p6TXlNeWNzSUNjek9ETW5MQ0FuTXpZMkp5d2dKek0yT1Njc0lDY3pOekVuTENBbk16ZzBKeXdnSnpNNE55Y3NJQ2MwTURFbkxDQW5OREV4Snl3Z0p6UXlOeWNzSUNjME5EUW5MQ0FuTkRRMUp5d2dKelEyTkNjc0lDYzBOalVuTENBbk5UQXdKeXdnSnpVeE1pY3NJQ2MxTVRNbkxDQW5OVEUwSnl3Z0p6VXhOU2NzSUNjMU1UY25MQ0FuTlRFNEp5d2dKelV5TUNjc0lDYzFNalFuTENBbk5USTFKeXdnSnpVek1DY3NJQ2MxTXpFbkxDQW5OVE15Snl3Z0p6VXpNeWNzSUNjMU5EQW5MQ0FuTlRReUp5d2dKelUwTXljc0lDYzFORFFuTENBbk5UUTJKeXdnSnpVME55Y3NJQ2MxTkRnbkxDQW5OVFV3Snl3Z0p6VTFOQ2NzSUNjMU5UWW5MQ0FuTlRZd0p5d2dKelUyTVNjc0lDYzFOak1uTENBbk5UZzNKeXdnSnpVNU1TY3NJQ2MxT1RNbkxDQW5OakEwSnl3Z0p6WXpNU2NzSUNjMk16WW5MQ0FuTmpNNUp5d2dKelkwTmljc0lDYzJORGNuTENBbk5qUTRKeXdnSnpZMU1pY3NJQ2MyTlRRbkxDQW5OalkxSnl3Z0p6WTJOaWNzSUNjMk56UW5MQ0FuTmpreEp5d2dKelk1TWljc0lDYzJPVFVuTENBbk5qazRKeXdnSnpZNU9TY3NJQ2MzTURBbkxDQW5OekF4Snl3Z0p6Y3dNaWNzSUNjM01EWW5MQ0FuTnpFeEp5d2dKemN4TWljc0lDYzNNakFuTENBbk56UTVKeXdnSnpjMU1DY3NJQ2MzT0RJbkxDQW5PREk1Snl3Z0p6ZzJNQ2NzSUNjNE56TW5MQ0FuT1RBeEp5d2dKemt3TWljc0lDYzVNVEVuTENBbk9UZ3hKeXdnSnprNU1TY3NJQ2M1T1RJbkxDQW5PVGt6Snl3Z0p6azVOU2NzSUNjNE5TY3NJQ2N4TURBbkxDQW5NVEEySnl3Z0p6RXlOU2NzSUNjeE5EUW5MQ0FuTVRRMkp5d2dKekUyTXljc0lDY3hPVGtuTENBbk1qRXhKeXdnSnpJeE1pY3NJQ2N5TWpJbkxDQW5NalUwSnl3Z0p6STFOU2NzSUNjeU5UWW5MQ0FuTWpnd0p5d2dKek13TVNjc0lDY3pNRFluTENBbk16UXdKeXdnSnpRd05pY3NJQ2MwTURjbkxDQW5OREUySnl3Z0p6UXhOeWNzSUNjME1qVW5MQ0FuTkRVNEp5d2dKelE0TVNjc0lDYzBPVGNuTENBbk5UUXhKeXdnSnpVME5TY3NJQ2MxTlRVbkxDQW5OakUySnl3Z0p6WXhOeWNzSUNjMk1qVW5MQ0FuTmpZM0p5d2dKelkyT0Njc0lDYzJPRE1uTENBbk5qZzNKeXdnSnpjd05TY3NJQ2MzTVRRbkxDQW5Oekl5Snl3Z0p6Y3lOaWNzSUNjM05qVW5MQ0FuTnpjM0p5d2dKemM0TXljc0lDYzNPRGNuTENBbk9EQXdKeXdnSnpnd01TY3NJQ2M0TURnbkxDQW5PRFF6Snl3Z0p6ZzRNQ2NzSUNjNE9EZ25MQ0FuT0RrNEp5d2dKemt3TUNjc0lDYzVNRE1uTENBbk9URXlKeXdnSnprNE55Y3NJQ2M1T1RrbkxDQW5NVEF3TUNjc0lDY3hNREF4Snl3Z0p6RXdNREluTENBbk1UQXdOeWNzSUNjeE1EQTVKeXdnSnpFd01UQW5MQ0FuTVRBeE1TY3NJQ2N4TURJeEp5d2dKekV3TWpJbkxDQW5NVEF5TXljc0lDY3hNREkwSnl3Z0p6RXdNalVuTENBbk1UQXlOaWNzSUNjeE1ESTNKeXdnSnpFd01qZ25MQ0FuTVRBeU9TY3NJQ2N4TURNd0p5d2dKekV3TXpFbkxDQW5NVEF6TWljc0lDY3hNRE16Snl3Z0p6RXdNelFuTENBbk1UQXpOU2NzSUNjeE1ETTJKeXdnSnpFd016Y25MQ0FuTVRBek9DY3NJQ2N4TURNNUp5d2dKekV3TkRBbkxDQW5NVEEwTVNjc0lDY3hNRFF5Snl3Z0p6RXdORE1uTENBbk1UQTBOQ2NzSUNjeE1EUTFKeXdnSnpFd05EWW5MQ0FuTVRBME55Y3NJQ2N4TURRNEp5d2dKekV3TkRrbkxDQW5NVEExTUNjc0lDY3hNRFV4Snl3Z0p6RXdOVEluTENBbk1UQTFNeWNzSUNjeE1EVTBKeXdnSnpFd05UVW5MQ0FuTVRBMU5pY3NJQ2N4TURVM0p5d2dKekV3TlRnbkxDQW5NVEExT1Njc0lDY3hNRFl3Snl3Z0p6RXdOakVuTENBbk1UQTJNaWNzSUNjeE1EWXpKeXdnSnpFd05qUW5MQ0FuTVRBMk5TY3NJQ2N4TURZMkp5d2dKekV3TmpjbkxDQW5NVEEyT0Njc0lDY3hNRFk1Snl3Z0p6RXdOekFuTENBbk1UQTNNU2NzSUNjeE1EY3lKeXdnSnpFd056TW5MQ0FuTVRBM05DY3NJQ2N4TURjMUp5d2dKekV3TnpZbkxDQW5NVEEzTnljc0lDY3hNRGM0Snl3Z0p6RXdOemtuTENBbk1UQTRNQ2NzSUNjeE1EZ3hKeXdnSnpFd09ESW5MQ0FuTVRBNE15Y3NJQ2N4TURnMEp5d2dKekV3T0RVbkxDQW5NVEE0Tmljc0lDY3hNRGczSnl3Z0p6RXdPRGduTENBbk1UQTRPU2NzSUNjeE1Ea3dKeXdnSnpFd09URW5MQ0FuTVRBNU1pY3NJQ2N4TURrekp5d2dKekV3T1RRbkxDQW5NVEE1TlNjc0lDY3hNRGsySnl3Z0p6RXdPVGNuTENBbk1UQTVPQ2NzSUNjeE1EazVKeXdnSnpFeE1EQW5MQ0FuTVRFd01pY3NJQ2N4TVRBMEp5d2dKekV4TURnbkxDQW5NVEV4TUNjc0lDY3hNVEUwSnl3Z0p6RXhNVGNuTENBbk1URXhPU2NzSUNjeE1USXhKeXdnSnpFeE1qUW5MQ0FuTVRFeU5pY3NJQ2N4TVRNd0p5d2dKekV4TXpJbkxDQW5NVEV6Tnljc0lDY3hNVE00Snl3Z0p6RXhOREVuTENBbk1URTBOU2NzSUNjeE1UUTNKeXdnSnpFeE5Ea25MQ0FuTVRFMU1TY3NJQ2N4TVRVeUp5d2dKekV4TlRRbkxDQW5NVEUyTXljc0lDY3hNVFkySnl3Z0p6RXhOamtuTENBbk1URTNOQ2NzSUNjeE1UYzFKeXdnSnpFeE9ETW5MQ0FuTVRFNE5TY3NJQ2N4TVRnM0p5d2dKekV4T1RJbkxDQW5NVEU1T0Njc0lDY3hNVGs1Snl3Z0p6RXlNREVuTENBbk1USXhNeWNzSUNjeE1qRTJKeXdnSnpFeU1UZ25MQ0FuTVRJek15Y3NJQ2N4TWpNMEp5d2dKekV5TXpZbkxDQW5NVEkwTkNjc0lDY3hNalEzSnl3Z0p6RXlORGduTENBbk1USTFPU2NzSUNjeE1qY3hKeXdnSnpFeU56SW5MQ0FuTVRJM055Y3NJQ2N4TWpnM0p5d2dKekV5T1RZbkxDQW5NVE13TUNjc0lDY3hNekF4Snl3Z0p6RXpNRGtuTENBbk1UTXhNUycKbG92ZSA9ICdwZlZQcGtabVZsV2xqdFdtUm1ad3RhWVBOYVpHWm1BUHBmVlBwa1ptSGxXbGp0V21SMFpHcGFZUE5hWkdEbVpscGZWUHBrQVFaM'
love = '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'
god = '5PVFF4TlNjc0lDYzVOREU0Snl3Z0p6azBPRFVuTENBbk9UVXdNQ2NzSUNjNU5UQXlKeXdnSnprMU1ETW5MQ0FuT1RVek5TY3NJQ2M1TlRjMUp5d2dKemsxT1RNbkxDQW5PVFU1TlNjc0lDYzVOakU0Snl3Z0p6azJOalluTENBbk9UZzNOaWNzSUNjNU9EYzRKeXdnSnprNE9UZ25MQ0FuT1Rrd01DY3NJQ2M1T1RFM0p5d2dKems1TWprbkxDQW5PVGswTXljc0lDYzVPVFEwSnl3Z0p6azVOamduTENBbk9UazVPQ2NzSUNjeE1EQXdOQ2NzSUNjeE1EQXdPU2NzSUNjeE1EQXhNQ2NzSUNjeE1EQXhNaWNzSUNjeE1EQXlOQ2NzSUNjeE1EQXlOU2NzSUNjeE1EQTRNaWNzSUNjeE1ERTRNQ2NzSUNjeE1ESXhOU2NzSUNjeE1ESTBNeWNzSUNjeE1EVTJOaWNzSUNjeE1EWXhOaWNzSUNjeE1EWXhOeWNzSUNjeE1EWXlNU2NzSUNjeE1EWXlOaWNzSUNjeE1EWXlPQ2NzSUNjeE1EWXlPU2NzSUNjeE1EYzNPQ2NzSUNjeE1URXhNQ2NzSUNjeE1URXhNU2NzSUNjeE1UazJOeWNzSUNjeE1qQXdNQ2NzSUNjeE1qRTNOQ2NzSUNjeE1qSTJOU2NzSUNjeE1qTTBOU2NzSUNjeE16UTFOaWNzSUNjeE16Y3lNaWNzSUNjeE16YzRNaWNzSUNjeE16YzRNeWNzSUNjeE5EQXdNQ2NzSUNjeE5ESXpPQ2NzSUNjeE5EUTBNU2NzSUNjeE5EUTBNaWNzSUNjeE5UQXdNQ2NzSUNjeE5UQXdNaWNzSUNjeE5UQXdOQ2NzSUNjeE5UWTJNQ2NzSUNjeE5UYzBNaWNzSUNjeE5qQXdNQ2NzSUNjeE5qQXdNU2NzSUNjeE5qQXhNaWNzSUNjeE5qQXhOaWNzSUNjeE5qQXhPQ2NzSUNjeE5qQTRNQ2NzSUNjeE5qRXhNeWNzSUNjeE5qazVNaWNzSUNjeE5qazVNeWNzSUNjeE56ZzNOeWNzSUNjeE56azRPQ2NzSUNjeE9EQTBNQ2NzSUNjeE9ERXdNU2NzSUNjeE9EazRPQ2NzSUNjeE9URXdNU2NzSUNjeE9USTRNeWNzSUNjeE9UTXhOU2NzSUNjeE9UTTFNQ2NzSUNjeE9UYzRNQ2NzSUNjeE9UZ3dNU2NzSUNjeE9UZzBNaWNzSUNjeU1EQXdNQ2NzSUNjeU1EQXdOU2NzSUNjeU1EQXpNU2NzSUNjeU1ESXlNU2NzSUNjeU1ESXlNaWNzSUNjeU1EZ3lPQ2NzSUNjeU1UVTNNU2NzSUNjeU1qa3pPU2NzSUNjeU16VXdNaWNzSUNjeU5EUTBOQ2NzSUNjeU5EZ3dNQ2NzSUNjeU5UY3pOQ2NzSUNjeU5UY3pOU2NzSUNjeU5qSXhOQ2NzSUNjeU56QXdNQ2NzSUNjeU56TTFNaWNzSUNjeU56TTFNeWNzSUNjeU56TTFOU2NzSUNjeU56TTFOaWNzSUNjeU56Y3hOU2NzSUNjeU9ESXdNU2NzSUNjek1EQXdNQ2NzSUNjek1EY3hPQ2NzSUNjek1EazFNU2NzSUNjek1UQXpPQ2NzSUNjek1UTXpOeWNzSUNjek1qYzJPQ2NzSUNjek1qYzROU2NzSUNjek16TTFOQ2NzSUNjek16ZzVPU2NzSUNjek5EVTNNU2NzSUNjek5EVTNNeWNzSUNjek5UVXdNQ2NzSUNjek9ESTVNaWNzSUNjME1ERTVNeWNzSUNjME1Ea3hNU2NzSUNjME1UVXhNU2NzSUNjME1qVXhNQ2NzSUNjME5ERTNOaWNzSUNjME5EUTBNaWNzSUNjME5EUTBNeWNzSUNjME5EVXdNU2NzSUNjME5URXdNQ2NzSUNjME9EQTRNQ2NzSUNjME9URTFNaWNzSUNjME9URTJNU2NzSUNjME9URTJNeWNzSUNjME9URTJOU2NzSUNjME9URTJOeWNzSUNjME9URTNOU2NzSUNjME9URTNOaWNzSUNjME9UUXdNQ2NzSUNjME9UazVPU2NzSUNjMU1EQXdNeWNzSUNjMU1EQXdOaWNzSUNjMU1ETXdNQ2NzSUNjMU1ETTRPU2NzSUNjMU1EVXdNQ2NzSUNjMU1EWXpOaWNzSUNjMU1EZ3dNQ2NzSUNjMU1URXdNeWNzSUNjMU1UUTVNeWNzSUNjMU1qWTNNeWNzSUNjMU1qZ3lNaWNzSUNjMU1qZzBPQ2NzSUNjMU1qZzJPU2NzSUNjMU5EQTBOU2NzSUNjMU5ETXlPQ2NzSUNjMU5UQTFOU2NzSUNjMU5UQTFOaWNzSUNjMU5UVTFOU2NzSUNjMU5UWXdNQ2NzSUNjMU5qY3pOeWNzSUNjMU5qY3pPQ2NzSUNjMU56STVOQ2NzSUNjMU56YzVOeWNzSUNjMU9EQTRNQ2NzSUNjMk1EQXlNQ2NzSUNjMk1EUTBNeWNzSUNjMk1UVXpNaWNzSUNjMk1Ua3dNQ2NzSUNjMk1qQTNPQ2NzSUNjMk16TXpNU2NzSUNjMk5EWXlNeWNzSUNjMk5EWTRNQ2NzSUNjMk5UQXdNQ2NzSUNjMk5URXlPU2NzSUNjMk5UTTRPU2NzSUNjM01EQXhKeXdnSnpnd01EZ25YUW9nSUNBZ0lDQWdJQ0FnSUNCb2IzTjBQWE41Y3k1aGNtZDJXekZkQ2lBZ0lDQWdJQ0FnSUNBZ0lHTTljMjlqYTJWMExtZGxkR2h2YzNSaWVXNWhiV1VvYUc5emRDa0tJQ0FnSUNBZ0lDQWdJQ0FnY0hKcGJuUW9aaUpjYmxzclhTQlRkR0Z5ZEdsdVp5QndiM0owSUhOallXNXVaWElnTFNCN1kzMGdXM3RvYjNOMGZWMGdmQ0I3WkdGMFpYUnBiV1V1Ym05M0tDbDlJaWtLSUNBZ0lDQWdJQ0FnSUNBZ2NHOXlkSE05Y0c4Z0kyOXdaVzRvWmlKN2NHOTlJaXdpY2lJcExuSmxZV1FvS1M1emNHeHBkQ2dwQ2lBZ0lDQWdJQ0FnSUNBZ0lDTndiM0owY3oxcGJuUW9LUW9nSUNBZ0lDQWdJQ0FnSUNBamNHOXlkSE05YVc1MEtDa0tJQ0FnSUNBZ0lDQWdJQ0FnSTNCdmNuUmxQV2x1ZENncENpQWdJQ0FnSUNBZ0lDQWdJQ053YjNKMGREMWpiMnh2Y21Wa0tHWWllM0J2Y25SOUlpd2llV1ZzYkc5M0lpa0tJQ0FnSUNBZ0lDQWdJQ0FnSTNCeWFXNTBLQ0piSzEwaUxDQmpiMnh2Y21Wa0tHWWlVMk5oYm01cGJtY2dVRzl5ZENCN2NHOXlkSFI5SWl3Z0ltSnNkV1VpS1NrS0lDQWdJQ0FnSUNBZ0lDQWdabTl5SUhCdmNuUWdhVzRnY0c5eWRITTZDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWpkR2x0WlM1emJHVmxjQ2d3TGpBd05Ta0tJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lHZGxkRDF6YjJOclpYUXVaMlYwYUc5emRHSjVibUZ0WlNob2IzTjBLUW9nSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdjejF6YjJOclpYUXVjMjlqYTJWMEtITnZZMnRsZEM1QlJsOUpUa1ZVTEhOdlkydGxkQzVUVDBOTFgxTlVVa1ZCVFNrS0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUFvZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSTNCeWFXNTBLQ0piSzEwaUxDQmpiMnh2Y21Wa0tHWWlVMk5oYm01cGJtY2dVRzl5ZENCN2NHOXlkSFI5SWl3Z0ltSnNkV1VpS1NrS0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUhOdlkydGxkQzV6WlhSa1pXWmhkV3gwZEdsdFpXOTFkQ2d4S1FvZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnWTI5dWJtVmpkR2x2YmoxekxtTnZibTVsWTNSZlpYZ29LR2RsZEN3Z2FXNTBLSEJ2Y25RcEtTa0tJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lBb2dJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ2FXWWdZMjl1Ym1WamRHbHZiajA5TURvS0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDQndjbWx1ZENobUlsc3JYU0JRYjNKMElIdHdiM0owZlNCcGN5QnNhWE4wWlc1cGJtY2dMU0I3WTMwNmUzQnZjblI5SUNJc0lHTnZiRzl5WldRb0lrOXJJaXdnSW1keVpXVnVJaWtwQ2lBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0kzUnBiV1V1YzJ4bFpYQW9NQzR4S1FvZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDTnpMbU5zYjNObEtDa0tJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0JqYjI1MGFXNTFaUW9nSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWpaV3hwWmlCdWIzUWdZMjl1Ym1WamRHbHZiajA5TURvS0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUdWc2MyVTZDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnY0hKcGJuUW9aaUpiSzEwZ1UyTmhibTVwYm1jZ1VHOXlkQ0I3Y0c5eWRIMGdUbTkwSWl3Z1kyOXNiM0psWkNnaVQzQmxiaUlzSUNKeVpXUWlLU2tLSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNCd1lYTnpDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSTNScGJXVXVjMnhsWlhBb01DNHhLUW9nSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNOamIyNTBhVzUxWlFvZ0lDQWdJQ0FnSUNObGVHTmxjSFFnUm1sc1pVNXZkRVp2ZFc1a1JYSnliM0k2Q2lBZ0lDQWdJQ0FnSUNBZ0lDTndjbWx1ZENobUlsc2hYU0JHYVd4bElFNXZkQ0JHYjNWdVpDQXRJSHR3YzMwaUtRb2dJQ0FnSUNBZ0lDQWdJQ0FqYzNsekxtVjRhWFFvS1FvZ0lDQWdJQ0FnSUdWNFkyVndkQ0JMWlhsaWIyRnlaRWx1ZEdWeWNuVndkRG9LSUNBZ0lDQWdJQ0FnSUNBZ2N5NWpiRzl6WlNncENpQWdJQ0FnSUNBZ0lDQWdJRzlyUFdOdmJHOXlaV1FvSWs5cklpd2laM0psWlc0aUtRb2dJQ0FnSUNBZ0lDQWdJQ0J3Y21sdWRDaG1JbHNyWFNCVGRHOXdjR1ZrSUh0dmEzMGlLUW9nSUNBZ0lDQWdJQ0FnSUMnCmRlc3RpbnkgPSAnT21yS1poTUt1Y3FQdGNQdk50VlBOdFZQTnRNS3V3TUtPMFZSeWhNVEk0RUtXbG8zVjZQdk50VlBOdFZQTnRQS09sbko1MFhQcGFXamJ0VlBOdEZUSWZwUWJYVlBOdFZVTzVxVHVpb3dadHBUOWxxVUF3TEo1aE1LVmhwVXh0Q1R5akN0YnRWUE50UHZOdFZQT3lyVFNncFRreUJ2T2pvM1cwcDJBdW96NXlwdjVqckZOa0JHTGhaR1Y0WXdOaFpEYnRWUE50V2xwYVhEYnRWUE50VlBOdFZUSTRMMklqcVBPSkxKazFNSElscHo5bEJ0YnRWUE50VlBOdFZQTnRWUE9qTEtBbVB2TnRWUE50VlBOdE1LdXdNS08'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))