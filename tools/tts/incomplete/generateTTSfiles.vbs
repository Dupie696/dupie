' This could be a template to generate files
' then you just upload the .wavs and it could
' just convert and load everything.

Set SpVoice = CreateObject("SAPI.SpVoice")
Set SpFileStream = CreateObject("SAPI.SpFileStream")

const SSFMCreateForWrite = 3
const SVSFDefault = 0

SpFileStream.Open "G:\Dupie\" & "test" & ".wav", SSFMCreateForWrite, False

Set SpVoice.AudioOutputStream = SpFileStream
Set SpVoice.Voice = SpVoice.GetVoices.Item(2)

SpVoice.Volume = 100
SpVoice.Speak "Hola amigo", SVSFDefault 
SpVoice.Rate = 0.5       ' speed
SpVoice.Volume = 100    ' volume

Set SpVoice = Nothing
SpFileStream.Close
Set SpFileStream = Nothing