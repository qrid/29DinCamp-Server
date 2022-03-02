import thecampy

soldier = thecampy.Soldier(
    '이규진',
    1999_04_05,
    2022_04_11,
    '육군훈련소'
)

def letter_build(letter):
    title, content = letter.get_header(), letter.content
    content = '<p>' + content.replace('\n', '</p><p>') + '</p>'
    content = content.replace('<p></p>', '<p>&nbsp</p>')

    return title, content


def test_send(letter):
    title, content = letter_build(letter)
    letter.subject = title
    letter.content = content

    letter.send_attempt_over = True
    letter.save()


def send(letter):
    try:
        # 작성된 글을 제목과 내용으로 분리시키기
        title, content = letter_build(letter)

        # 메제지 개체 작성
        msg = thecampy.Message(title, content)

        # 내 계정 가져오기
        thecamp_client = thecampy.Client('rbwls5567@naver.com', 'rbwls&*79&*79')

        # 내 계정으로 나에게 메세지 개체 보내기
        send_result = thecamp_client.send_message(soldier, msg)

        # 전송 결과를 저장하기
        letter.sent = send_result
        print("전송했습니다.")
        return True

    except Exception as p:
        print("전송 실패했습니다.")
        return False

    finally:
        letter.send_attempt_over = True
        letter.save()
