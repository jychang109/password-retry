password = 'a123456'
i = 3
while i > 0:
	pw = input('請輸入密碼(最多三次)：')
	if pw == password:
		print('登入成功')
		break
	else:
		i = i - 1
		print('密碼錯誤！還有 ', i, ' 次機會！')