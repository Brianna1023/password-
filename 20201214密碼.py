password = 'brianna1023'
i = 3
while i > 0:
	psd = input('請問帳號密碼:')
	if psd == password:
		print('登入成功!!')
		break
	else:
		i = i - 1
		print('密碼錯誤')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('沒機會嘗試了!要鎖帳號了!')
		
