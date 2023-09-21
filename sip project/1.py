from pyVoIP.VoIP import VoIPPhone, InvalidStateError, CallState,VoIPCall
import time
import wave,pyVoIP

# pyVoIP.DEBUG = True

def answer(call):
    print("4",phone.getStatus())

    try:
        f = wave.open('announcment.wav', 'rb')
        frames = f.getnframes()
        data = f.readframes(frames)

        f.close()

        call.answer()
        call.write_audio(data)  # This writes the audio data to the transmit buffer, this must be bytes.

        stop = time.time() + (frames / 8000)  # frames/8000 is the length of the audio in seconds. 8000 is the hertz of PCMU.

        while time.time() <= stop and call.state == CallState.ANSWERED:
            time.sleep(0.1)
        call.hangup()
    except InvalidStateError:
        pass
    except:
        call.hangup()


if __name__ == "__main__":
    # phone = VoIPPhone(<SIP Server IP>, <SIP Server Port>, <SIP Server Username>, <SIP Server Password>, myIP=<Your computers local IP>, callCallback=answer)

    phone=VoIPPhone("192.168.52.131", 5060,"500", "123",myIP="192.168.52.1",callCallback=answer)
    phone.start()
    print("Obj : ",phone)
    print("1",phone.getStatus())
    get_state=phone.call(400)

    print("state : ",get_state.text)
    print("2",phone.getStatus())
    input('Press enter to disable the phone')



    phone.stop()
    print("3",phone.getStatus())