""" Menu
- Criação de Chaves Publica e Privada
	- Criação ou Ingresso em Cadeia existente
		- Visualizar Post's
			- Curtir ou descurtir Post
		- Publicar Post
		- Reputação na Cadeia
 """

""" import subprocess
import sys

result = subprocess.run(
    ["freechains-host", "--port=8331", "start", "/tmp/othost&"], capture_output=True, text=True
)
p = subprocess.Popen(["freechains-host", 'now'], stdout=None, stderr=subprocess.STDOUT);
print("stdout:", p.stdout)
print("stderr:", p.stderr) """

from os import putenv
import subprocess
import sys

""" def checkKey(privateKey,publicKey):
	if privateKey != '' and publicKey != '':
		return True
	return False """

def startHost(hostPort, dirPath):
	freeExec = subprocess.Popen(["freechains-host", '--port='+hostPort, 'start', dirPath], stdout=None, stderr=subprocess.STDOUT);
	print("stdout:", freeExec.stdout)
	print("stderr:", freeExec.stderr)

def newKey(passwrd):
	freeExec = subprocess.run(
		["freechains", "crypto", "pubpvt", passwrd], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)
	
	return freeExec.stdout.split(' ')

def joinChain(chainName, publicKey):
	
	chain = chainName
	print(type(chain))
#	freeExec = subprocess.run(
#		["freechains", "chains", "join", chain, publicKey], capture_output=True, text=True
#	)

#	print("stderr:", freeExec.stderr)
#	return freeExec.stdout

def leaveChain(chainName):
	freeExec = subprocess.run(
		["freechains", "chains", "leave", "#"+chainName], capture_output=True, text=True
	)

	print("stderr:", freeExec.stderr)

def listChain():
	freeExec = subprocess.run(
		["freechains", "chains", "list"], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)
	
	return freeExec.stdout

def newPost(chainName, privateKey, pathFile):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+chainName, 'post', '--sign=' + privateKey, 'file', pathFile], capture_output=True, text=True
	)
	print("stderr:", freeExec.stderr)

	return freeExec.stdout

def getPost(chainName, post, outputFile):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+chainName, 'get', 'payload', post, 'file', outputFile], capture_output=True, text=True
	)
	print("stderr:", freeExec.stderr)

	return freeExec.stdout

def likePost(chainName, post, privateKey, msg):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+chainName, 'like', post, '--sign=' + privateKey, '--why='+ msg], capture_output=True, text=True
	)
	print("stderr:", freeExec.stderr)

	return freeExec.stdout

def listPosts(chainName):
	chain = "#"+chainName
	freeExec = subprocess.run(
		['freechains', 'chain', chain, 'heads'], capture_output=True, text=True
	)
	print("stderr:", freeExec.stderr)

	ps = freeExec.stdout.split(' ')
	listPosts = []
	for i in ps:
		listPosts.append(i)

	return listPosts

def listBlockedPosts(chainName):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+chainName, 'heads', 'blocked'], capture_output=True, text=True
	)
	print("stderr:", freeExec.stderr)

	ps = freeExec.stdout.split(' ')
	listPosts = []
	for i in ps:
		listPosts.append(i)

	return listPosts

def dislikePost(chainName, post, privateKey, msg):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+chainName, 'dislike', post, '--sign=' + privateKey, '--why='+ msg], capture_output=True, text=True
	)
	print("stderr:", freeExec.stderr)

	return freeExec.stdout

def getRepsPost(chainName, post):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+chainName, 'reps', post], capture_output=True, text=True
	)
	print("stderr:", freeExec.stderr)

	return freeExec.stdout

def getRepsUser(chainName, publicKey):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+chainName, 'reps', publicKey], capture_output=True, text=True
	)
	print("stderr:", freeExec.stderr)

	return freeExec.stdout

def sendChainHost(chainName, hostIp, hostPort, destIp, destPort):
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'peer', destIp+':'+destPort, 'send', "#"+chainName], capture_output=True, text=True
	)
	print("stderr:", freeExec.stderr)

	return freeExec.stdout

def recvChainHost(chainName, hostIp, hostPort, origIp, origPort):
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'peer', origIp+':'+origPort, 'recv', "#"+chainName], capture_output=True, text=True
	)
	print("stderr:", freeExec.stderr)

	return freeExec.stdout

def updatePostList(newsPosts, posts):
	for post in newsPosts:
		if post in posts:
			continue
		newPost = (post, '', '')
		posts.append(newPost)

def updateBlockedPostList():
	newBlockedPosts = listBlockedPosts(chainName)
	blockedPosts = []
	for post in newBlockedPosts:
		if post in posts:
			continue
		blockedPost = (post, '', '')
		blockedPosts.append(blockedPost)

def print_menu(menuType, posts=None, chainName=None):
	if menuType == 1:
		print('Bem vindo ao Forum.\n')
		
		print('Selecione uma opção no menu abaixo:\n')

		print('1 - Criar novo par de Chaves.\n2 - Sair')
	
	if menuType == 2:
		print('\nForum Responde Ai.\n')
		
		print('Selecione uma opção no menu abaixo:\n')
		
		print('1 - Listar disciplinas.\n2 - Ingressar em uma nova/existente disciplina.\n3 - Sair da disciplina\n4 - Voltar ao menu anterior.\n5 - Sair')
	
	if menuType == 3:
		print('\nForum Responde Ai.\n')

		newsPosts = listPosts(chainName)
		updatePostList(newsPosts, posts)

		print('Posts:\n')
		if len(posts) != 0:
			for post in posts:
				print('File Name: '+post[(1)]+' Hash: '+post[(0)]+'\n')
		else:
			print('Sem posts na Disciplina\n')
		
		print('Blocked Posts:\n')
		blockedPosts = updateBlockedPostList()

		if len(blockedPosts) != 0:
			for post in blockedPosts:
				print('File Name: '+post[(1)]+' Hash: '+post[(0)]+'\n')
		else:
			print('Sem posts bloqueados na Disciplina\n')
	
		print('Selecione uma opção no menu abaixo:\n')
		
		print('1 - Receber novos Post.\n2 - Enviar novos Post.\n3 - Visualizar post.\n4 - Criar novo post.\n5 - Curtir Post.\n6 - Descurtir Post.\n7 - Visualizar reputacao.\n8 - Voltar ao menu anterior.\n9 - Sair')
	
def act1Menu1():
	print('Criação de Chave\n')

	passwrd = input('Insira sua senha segura: ')
	publicKey,privateKey = newKey(passwrd)

	menuType = 2
	
	return privateKey, publicKey, menuType

def act1Menu2():
	chains = listChain()
	if chains != '':
		print('\nDisciplinas:\n')
		print(chains)
	else:
		print('Não existem Disciplinas disponiveis')

def act2Menu2(publicKey):
	print('\nIngressar em Disciplina\n')
	
	chainName = input('Insira o nome da Disciplina: ')
	chain = joinChain(chainName, publicKey)

	menuType = 3

	return chain, chainName, menuType

def act3Menu2():
	chains = listChain()
	if chains != '':
		print('\nSair da Disciplina\n')
		
		chainName = input('Insira o nome da disciplina: ')
		leaveChain(chainName)
	else:
		print('Não existem disciplinas disponiveis')

def act4Menu2():
	menuType = 1
	return menuType

def act1Menu3(chainName):
	print('\nReceber Posts\n')
	
	hostIp = input('Insira o seu host ip: ')
	hostPort = input('Insira a porta de execucao: ')
	origIp = input('Insira o host ip de origem: ')
	origPort = input('Insira a porta de execucao de origem: ')
	recvChainHost(chainName, hostIp, hostPort, origIp, origPort)

def act2Menu3(chainName):
	print('\nEnviar Posts\n')
	
	hostIp = input('Insira o seu host ip: ')
	hostPort = input('Insira a porta de execucao: ')
	destIp = input('Insira o host ip de destino: ')
	destPort = input('Insira a porta de execucao de destino: ')
	sendChainHost(chainName, hostIp, hostPort, destIp, destPort)

def act3Menu3(chainName):
	print('\nVisualizar Post\n')

	post = input('Insira o id do post: ')
	outputFile = input('Insira o path de saida do arquivo: ')
	print(getPost(chainName, post, outputFile))
	print('\nA Reputacao do post é '+getRepsPost(chainName, post))

def act4Menu3(chainName, privateKey, posts):
	print('\nCriar Post\n')

	nameFile = input('Insira o nome do arquivo: ')
	pathFile = input('Insira o path do arquivo: ')

	#print(newPost(chainName, privateKey, pathFile))
	
	post = (newPost(chainName, privateKey, pathFile), nameFile, privateKey)
	posts.append(post)


def act5Menu3(chainName, privateKey):
	print('\nCurtir Post\n')
	
	post = input('Insira o id do post: ')
	msg = input('Insira o motivo do like: ')

	likePost(chainName,post,privateKey,msg)

def act6Menu3(chainName, privateKey):
	print('\nDescurtir Post\n')
	
	post = input('Insira o id do post: ')
	msg = input('Insira o motivo do dislike: ')

	dislikePost(chainName,post,privateKey,msg)

def act7Menu3(chainName, publicKey):
	print('\nVisualizar Reputacao\n')

	print('A sua reputação na disciplina '+chainName+' é '+getRepsUser(chainName,publicKey))

def act8Menu3():
	menuType = 2
	return menuType

def startMenu():
    global privateKey
    global publicKey
    global menuType
    global exit	
    while menuType == 1:
        print_menu(menuType)
        selection = input("Sua escolha: ")
        if "1" == selection:
            privateKey, publicKey, menuType = act1Menu1()
        if "2" == selection:
            exit = True
            return

def chainMenu():
    global privateKey
    global publicKey
    global menuType
    global chain
    global chainName
    global exit
    global posts
    while menuType == 2:
        print_menu(menuType, posts)
        selection = input("Sua escolha: ")
        if "1" == selection:
            act1Menu2()
        if "2" == selection:
            chain, chainName, menuType = act2Menu2(publicKey)
        if "3" == selection:
            act3Menu2()
        if "4" == selection:
            menuType = act4Menu2()
        if "5" == selection:
            exit = True
            return

def postMenu():
    global privateKey
    global publicKey
    global menuType
    global chainName
    global exit
    while menuType == 3:
        print_menu(menuType)
        selection = input("Sua escolha: ")
        if "1" == selection:
            act1Menu3(chainName)
        if "2" == selection:
            act2Menu3(chainName)
        if "3" == selection:
            act3Menu3(chainName)
        if "4" == selection:
            act4Menu3(chainName, privateKey)
        if "5" == selection:
            act5Menu3(chainName, privateKey)
        if "6" == selection:
            act6Menu3(chainName, privateKey)
        if "7" == selection:
            act7Menu3(chainName, publicKey)
        if "8" == selection:
            menuType = act8Menu3()
        if "9" == selection:
            exit = True
            return

if __name__ == "__main__":
	
	#hostPort = input('Insira a porta de execucao: ')
	#dirPath = input('Insira o diretorio de execucao: ')
	#startHost(hostPort, dirPath)
	
	privateKey, publicKey, chain, chainName = '', '', '', ''
	posts = []
	exit = False
	menuType = 1
	while exit == False:
		if menuType == 1:
			startMenu()
		elif menuType == 2:
			chainMenu()
		elif menuType == 3:
			postMenu()
