' This could be a template to generate files
' then you just upload the .wavs and it could
' just convert and load everything.

Set Lang1Voice = CreateObject("SAPI.SpVoice")
Set Lang1FileStream = CreateObject("SAPI.SpFileStream")
Set Lang2Voice = CreateObject("SAPI.SpVoice")
Set Lang2FileStream = CreateObject("SAPI.SpFileStream")

const SSFMCreateForWrite = 3
const SVSFDefault = 0

dim lang0index(3)
dim lang1words(3)
dim lang2words(3)
lang0index(0) = 1100
lang1words(0) = "Welcome Home"
lang2words(0) = "Bienvenido a casa"
lang0index(0) = 1101
lang1words(1) = "Where are you?"
lang2words(1) = "¿Donde está?"
lang0index(0) = 1102
lang1words(2) = "What are you doing?"
lang2words(2) = "¿Que estas haciendo?"
lang1speaker = 0 ' English
lang2speaker = 2 ' Spanish
lang1code = "EN"
lang2code = "ES"
lang1rate = 0.5
lang2rate = 0.5

for lcv = 0 to ubound(lang0index) - 1
    Lang1FileStream.Open "G:\Dupie\" & lcv & "-" & lang1code & ".wav", SSFMCreateForWrite, False
    Lang2FileStream.Open "G:\Dupie\" & lcv & "-" & lang2code & ".wav", SSFMCreateForWrite, False

    Set Lang1Voice.AudioOutputStream = Lang1FileStream
    Set Lang1Voice.Voice = Lang1Voice.GetVoices.Item(lang1speaker)

    Set Lang2Voice.AudioOutputStream = Lang2FileStream
    Set Lang2Voice.Voice = Lang1Voice.GetVoices.Item(lang2speaker)

    Lang1Voice.Speak lang1words(lcv), SVSFDefault 
    Lang1Voice.Rate = lang1rate
    Lang1Voice.Volume = 100

    Lang2Voice.Speak lang2words(lcv), SVSFDefault 
    Lang2Voice.Rate = lang2rate
    Lang2Voice.Volume = 100

    Lang1FileStream.Close
    Lang2FileStream.Close

next

Set Lang1Voice = Nothing
Set Lang1FileStream = Nothing
