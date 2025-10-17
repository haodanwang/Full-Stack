# def send_email(recipient, subject, content, **kwargs):
#     print("连接服务器")
#     print(f"收件人邮箱{recipient}")
#     print(f"主题{subject}")
#     print(f"内容{content}")
#     print("抄送", kwargs)
#     cc = kwargs.get("cc")
#     bcc = kwargs.get("bcc")
#     if cc:
#         print("抄送人", cc)
#     if bcc:
#         print("秘送人", bcc)
#
#
# r = "alex@qq.com"
# s = "重要通知"
# c = "您已被解雇"
# send_email(r, s, c, cc="alex@com", bcc="rain@qq.com")
# send_email(r, s, c)

# * args和*kwargs


# def info(a, *b, **c):
#     print(a)
#     print(b)
#     print(c)
#
#
# info(1, 2, 3, 4, 5, 6, x=1)
