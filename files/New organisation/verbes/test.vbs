Dim msg, sapi
 MsgBox ("ecrire le texte a prononcer :-)")
 msg1 = InputBox ("Enter")
 Set sapi = CreateObject ("sapi.spvoice")
 sapi.Speak msg1
