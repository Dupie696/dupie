'########################################################
'# This is a test file to be ran on your windows box
'# 
'# Running this script will allow you to test all your 
'# installed voices, intended to be used with gneration 
'# script
'#
'#
'#  NOTE: VBS does not support UTF-8. This file will need
'#        to be saved in UTF-16 or UTF-16 LE to support
'#        unicode characters fr different languages
'#
'#########################################################


' loads microsofts speech API
Set SpVoice = CreateObject("sapi.spvoice")

' Sets a default string for testing languages
Dim voice_index, ttsMessage, SpVoice, aggString, inputResponse, inputTTS
ttsMessage = "Hello	Hallo	Hej	你好	Hola	Bonjour	مرحبًا 	こんにちは	안녕	Привет"

' Generates summary of installed voices
For voice_index = 0 To SpVoice.GetVoices.Count - 1
    Set SpVoice.Voice = SpVoice.GetVoices.Item(voice_index)
    aggString = aggString & (voice_index & ") " & SpVoice.Voice.GetDescription) & vbCrLf
Next

' Displays summary
inputResponse = InputBox("Your sound profiles are as follows: " & vbCrLf & vbCrLf & aggString & vbCrLf & vbCrLf & "Which of the voices would you like to hear? Enter number or type all for demo.", "Dupie TTS Test Script", "all")

' Displays default test message, with option to customize at runtime
inputTTS = InputBox("what message would you like to Text-to-Speech(TTS)?", "Dupie TTS Test Script", ttsMessage)

If "all" = inputResponse Then
    ' Cycles throw all voices demoing the message
    For voice_index = 0 To SpVoice.GetVoices.Count - 1
        ' specifies voice
        Set SpVoice.Voice = SpVoice.GetVoices.Item(voice_index)
        ' speaks the message
        SpVoice.Speak inputTTS
        ' break point to exit the loop and summary message of what you heard
        If vbNo = MsgBox("You just heard profile #" & voice_index & ": " & vbCrLf & vbCrLf & SpVoice.Voice.GetDescription & vbCrLf & vbCrLf & vbCrLf & "Would you like to continue listening to the demo of all the voices?", vbYesNo, "Dupie TTS Test Script") Then Exit For
    Next

ElseIf Str(inputResponse) = Str(Int(inputResponse)) Then

    ' loads selected voice
    voice_index = Int(inputResponse)
    Set SpVoice.Voice = SpVoice.GetVoices.Item(voice_index)
    ' speaks the message
    SpVoice.Speak inputTTS
    ' summary message of what you heard
    MsgBox "You just heard profile #" & voice_index & ": " & vbCrLf & vbCrLf & SpVoice.Voice.GetDescription, , "Dupie TTS Test Script"

End If
