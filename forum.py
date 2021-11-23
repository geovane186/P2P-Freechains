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

class User:
	def __init__(self):
		self.password = ''
		self.publicKey = ''
		self.privateKey = ''
		self.reputation = ''
	
	#Getter
	def getPassword(self):
		return self.password
	
	def getPublicKey(self):
		return self.publicKey
	
	def getPrivateKey(self):
		return self.privateKey
	
	def getReputation(self):
		return self.reputation
	
	#Setter
	def setPassword(self, value):
		self.password = value
	
	def setPublicKey(self, value):
		self.publicKey = value
	
	def setPrivateKey(self, value):
		self.privateKey = value
		
	def setReputation(self, value):
		self.reputation = value
	
class Post:
	def __init__(self):
		self.fileName = ''
		self.hash = ''
		self.privateKey = ''
		self.reputation = ''
	
	#Getter
	def getFileName(self):
		return self.fileName
	
	def getFilePath(self):
		return self.filePath
	
	def getHash(self):
		return self.hash
	
	def getPrivateKey(self):
		return self.privateKey
	
	def getReputation(self):
		return self.reputation
	
	#Setter
	def setFileName(self, value):
		self.fileName = value
	
	def setFilePath(self, value):
		self.filePath = value
	
	def setHash(self, value):
		self.hash = value
	
	def setPrivateKey(self, value):
		self.privateKey = value
		
	def setReputation(self, value):
		self.reputation = value

class Chain:
	def __init__(self):
		self.name = ''
		self.hash = ''
		self.pionerKey = ''
	
	#Getter
	def getName(self):
		return self.name
	
	def getHash(self):
		return self.hash
	
	def getPionerKey(self):
		return self.pionerKey
	
	#Setter
	def setName(self, value):
		self.name = value
	
	def setHash(self, value):
		self.hash = value
	
	def setPionerKey(self, value):
		self.pionerKey = value

""" def checkKey(privateKey,publicKey):
	if privateKey != '' and publicKey != '':
		return True
	return False """

def startHost(hostPort, dirPath):
	freeExec = subprocess.Popen(["freechains-host", '--port='+hostPort, 'start', dirPath], stdout=None, stderr=subprocess.STDOUT);
	print("stdout:", freeExec.stdout)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

def newKey(passwrd):
	freeExec = subprocess.run(
		["freechains", "crypto", "pubpvt", passwrd], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)
	
	return freeExec.stdout.split(' ')

def joinChain(chainName, publicKey):

	freeExec = subprocess.run(
		["freechains", "chains", "join", '#'+str(chainName), publicKey], capture_output=True, text=True
	)
	print(freeExec.args)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)
	return freeExec.stdout

def leaveChain(chainName):
	freeExec = subprocess.run(
		["freechains", "chains", "leave", "#"+str(chainName)], capture_output=True, text=True
	)

	if freeExec.stderr:
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
		['freechains', 'chain', "#"+str(chainName), 'post', '--sign=' + privateKey, 'file', pathFile], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def getPost(chainName, post, outputFile):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+str(chainName), 'get', 'payload', post, 'file', outputFile], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def likePost(chainName, post, privateKey, msg):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+str(chainName), 'like', post, '--sign=' + privateKey, '--why='+ msg], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def getBlockInfo(chainName, hash):
	
	freeExec = subprocess.run(
		["freechains", "chain", '#'+str(chainName), 'get', 'block', hash], capture_output=True, text=True
	)
	print(freeExec.args)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def isPost(chainName, hash):
	hash = '0_214ED611E8E377DEB8D0F35EA15E457181418739E1158A8C9082A124CF26E6CD'
	res = getBlockInfo(chainName, hash)
	print(res)
	return False

def listPosts(chainName):
	freeExec = subprocess.run(
		['freechains', 'chain', '#'+str(chainName), 'heads'], capture_output=True, text=True
	)
	print(freeExec.args)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	posts = freeExec.stdout.split(' ')

	listPosts = []
	for post in posts:
		print(post)
		res = getBlockInfo(chainName,post)
		print(res)
		#if isPost(chainName, i):
	#		listPosts.append(i)
	return listPosts

def listBlockedPosts(chainName):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+str(chainName), 'heads', 'blocked'], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	ps = freeExec.stdout.split(' ')
	listPosts = []
	for i in ps:
		listPosts.append(i)

	return listPosts

def dislikePost(chainName, post, privateKey, msg):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+str(chainName), 'dislike', post, '--sign=' + privateKey, '--why='+ msg], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def getRepsPost(chainName, post):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+str(chainName), 'reps', post], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def getRepsUser(chainName, publicKey):
	freeExec = subprocess.run(
		['freechains', 'chain', "#"+str(chainName), 'reps', publicKey], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def sendChainHost(chainName, hostIp, hostPort, destIp, destPort):
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'peer', destIp+':'+destPort, 'send', "#"+str(chainName)], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def recvChainHost(chainName, hostIp, hostPort, origIp, origPort):
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'peer', origIp+':'+origPort, 'recv', "#"+str(chainName)], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def updatePostList(newsPosts, posts):
	for newPost in newsPosts:
		p = Post()
		p.setHash(newPost)
		#newPost = (post, '', '')
		for post in posts:
			if p.getHash() == post.getHash():
				continue
		posts.append(p)

def updateBlockedPostList(chainName):
	newBlockedPosts = listBlockedPosts(chainName)
	blockedPosts = []
	for post in newBlockedPosts:
		blockedPost = (post, '', '')
		if blockedPost in posts:
			continue
		blockedPosts.append(blockedPost)

def print_menu(menuType, posts=None, chainName=None, blockedPosts=None, publicKey=None):
	if menuType == 1:
		print('Bem vindo ao Forum.\n')
		
		print('Selecione uma opção no menu abaixo:\n')

		print('1 - Criar novo par de Chaves.\n2 - Sair')
	
	if menuType == 2:
		print('\nForum Responde Ai.\n')

		print('User: '+ str(publicKey)+'\n')
		
		print('Selecione uma opção no menu abaixo:\n')
		
		print('1 - Listar disciplinas.\n2 - Ingressar em uma nova/existente disciplina.\n3 - Sair da disciplina\n4 - Voltar ao menu anterior.\n5 - Sair')
	
	if menuType == 3:
		print('\nForum Responde Ai.\n')

		print('User: '+ str(publicKey)+'\n')

		newsPosts = listPosts(chainName)
		updatePostList(newsPosts, posts)

		print('Posts:\n')
		if posts:
			for post in posts:
				print('File Name: '+post[(1)]+' Hash: '+post[(0)]+'\n')
		else:
			print('Sem posts na Disciplina\n')
		
		print('Blocked Posts:\n')
		blockedPosts = updateBlockedPostList(chainName)

		if blockedPosts:
			for post in blockedPosts:
				print('File Name: '+post[(1)]+' Hash: '+post[(0)]+'\n')
		else:
			print('Sem posts bloqueados na Disciplina\n')
	
		print('Selecione uma opção no menu abaixo:\n')
		
		print('1 - Receber novos Post.\n2 - Enviar novos Post.\n3 - Visualizar post.\n4 - Criar novo post.\n5 - Curtir Post.\n6 - Descurtir Post.\n7 - Visualizar reputacao.\n8 - Voltar ao menu anterior.\n9 - Sair')
	
def act1Menu1():
	print('Criação de Chave\n')

	password = input('Insira sua senha segura: ')
	publicKey,privateKey = newKey(password)

	menuType = 2
	
	return password, privateKey, publicKey, menuType

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

def act3Menu3(chainName, posts):
	print('\nVisualizar Post\n')

	hash = input('Insira o id do post: ')
	outputFile = input('Insira o path de saida do arquivo: ')
	for post in posts:
		if hash == post.getHash():
			print(getPost(chainName, hash, outputFile))
			post.setReputation(getRepsPost(chainName, hash))
			#print('\nA Reputacao do post é '+str(getRepsPost(chainName, hash)))
			print('\nA Reputacao do post é '+str(post.getReputation()))
		else:
			print('Post não encontrado.')

def act4Menu3(chainName, privateKey, posts):
	print('\nCriar Post\n')

	post = Post()

	post.setFileName(input('Insira o nome do arquivo: '))
	post.setFilePath = input('Insira o path do arquivo: ')
	post.setPrivateKey(privateKey)
	post.setReputation('0')
	
	post.setHash((newPost(chainName, privateKey, post.getFilePath()), post.getFileName(), post.getPrivateKey()))
	posts.append(post)


def act5Menu3(chainName, privateKey, posts):
	print('\nCurtir Post\n')
	
	hash = input('Insira o id do post: ')
	msg = input('Insira o motivo do like: ')
	for post in posts:
		if hash == post.getHash():
			likePost(chainName, hash, privateKey, msg)
		else:
			print('Post não encontrado.')

def act6Menu3(chainName, privateKey, posts):
	print('\nDescurtir Post\n')
	
	hash = input('Insira o id do post: ')
	msg = input('Insira o motivo do dislike: ')
	for post in posts:
		if hash == post.getHash():
			dislikePost(chainName, hash, privateKey, msg)
		else:
			print('Post não encontrado.')

def act7Menu3(chainName, publicKey):
	print('\nVisualizar Reputacao\n')
	
	print('A sua reputação na disciplina '+chainName+' é '+getRepsUser(chainName, publicKey))

def act8Menu3():
	menuType = 2
	return menuType

def startMenu():
    global user
    #global privateKey
    #global publicKey
    global menuType
    global exit	
    while menuType == 1:
        print_menu(menuType)
        selection = input("Sua escolha: ")
        if "1" == selection:
            password, privateKey, publicKey, menuType = act1Menu1()
            user.setPassword(password)
            user.setPublicKey(publicKey)
            user.setPrivateKey(privateKey)
        if "2" == selection:
            exit = True
            return

def chainMenu():
    global user
    global chain
    #global privateKey
    #global publicKey
    global menuType
#   global chain
#    global chainName
    global posts
    global exit
    while menuType == 2:
        print_menu(menuType, publicKey=user.getPublicKey())
        selection = input("Sua escolha: ")
        if "1" == selection:
            act1Menu2()
        if "2" == selection:
            hash, chainName, menuType = act2Menu2(user.getPublicKey())
            chain.setName(chainName)
            chain.setHash(hash)
            chain.setPionerKey(user.getPublicKey())
        if "3" == selection:
            act3Menu2()
        if "4" == selection:
            menuType = act4Menu2()
        if "5" == selection:
            exit = True
            return

def postMenu():
    global user
    global chain
#    global privateKey
#    global publicKey
    global menuType
#    global chainName
    global blockedPosts
    global posts
    global exit
    while menuType == 3:
        print_menu(menuType, posts, chain.getName(), blockedPosts, publicKey=user.getPublicKey())
        selection = input("Sua escolha: ")
        if "1" == selection:
            act1Menu3(chain.getName())
        if "2" == selection:
            act2Menu3(chain.getName())
        if "3" == selection:
            act3Menu3(chain.getName(), posts)
        if "4" == selection:
            act4Menu3(chain.getName(), user.getPrivateKey(), posts)
        if "5" == selection:
            act5Menu3(chain.getName(), user.getPrivateKey(), posts)
        if "6" == selection:
            act6Menu3(chain.getName(), user.getPrivateKey(), posts)
        if "7" == selection:
            act7Menu3(chain.getName(), user.getPublicKey())
        if "8" == selection:
            menuType = act8Menu3()
        if "9" == selection:
            exit = True
            return

if __name__ == "__main__":
	
	#hostPort = input('Insira a porta de execucao: ')
	#dirPath = input('Insira o diretorio de execucao: ')
	#startHost(hostPort, dirPath)
	
	#privateKey, publicKey, chain, chainName = '', '', '', ''
	user = User()
	chain = Chain()
	posts = []
	blockedPosts = []
	exit = False
	menuType = 1
	while exit == False:
		if menuType == 1:
			startMenu()
		elif menuType == 2:
			chainMenu()
		elif menuType == 3:
			postMenu()
