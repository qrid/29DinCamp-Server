import thecampy

'''
soldier = thecampy.Soldier('이규진', 1999_04_05, 2022_04_07, '육군훈련소')
user_id = 'rbwls5567@naver.com'
with open('thecampy_pw.secret', 'r') as f:
    user_pw = f.read().strip()
'''


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
        title, content = letter_build(letter)

        msg = thecampy.Message(title, content)
        tc = thecampy.Client(user_id, user_pw)

        tc.get_soldier(soldier)
        send_result = tc.send_message(soldier, msg)

        letter.sent = send_result
        return True

    except Exception as p:
        return False

    finally:
        letter.send_attempt_over = True
        letter.save()
