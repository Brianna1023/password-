password = 'brianna1023'
i = 3
while True:
	psd = input('請問帳號密碼:')
	if psd == password:
		print('登入成功!!')
		break
	else:
		i = i - 1
		print('密碼錯誤還有', i, '次機會')
		if i == 0:
			break
