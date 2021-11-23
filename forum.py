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
import json 
import time

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
		self.filePath = ''
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

def startHost(hostPort, dirPath):
	global freeStart
	freeStart = subprocess.Popen(["freechains-host", '--port='+hostPort, 'start', dirPath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT);
	if freeStart.stderr:
		print("stderr:", freeStart.stderr)

def newKey(passwrd):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		["freechains", '--host='+hostIp+':'+hostPort, "crypto", "pubpvt", passwrd], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)
	
	return freeExec.stdout.split(' ')

def joinChain(chainName, publicKey):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		["freechains", '--host='+hostIp+':'+hostPort, "chains", "join", '#'+str(chainName), publicKey], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)
	return freeExec.stdout

def leaveChain(chainName):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		["freechains", '--host='+hostIp+':'+hostPort, "chains", "leave", "#"+str(chainName)], capture_output=True, text=True
	)

	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

def listChain():
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		["freechains", '--host='+hostIp+':'+hostPort, "chains", "list"], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)
	
	return freeExec.stdout

def newPost(chainName, privateKey, pathFile):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'chain', "#"+str(chainName), 'post', '--sign=' + privateKey, 'file', pathFile], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def getPost(chainName, post, outputFile):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'chain', "#"+str(chainName), 'get', 'payload', post, 'file', outputFile], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def likePost(chainName, post, privateKey, msg):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'chain', "#"+str(chainName), 'like', post, '--sign=' + privateKey, '--why='+ msg], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def getBlockInfo(chainName, hash):
	global hostIp
	global hostPort	
	freeExec = subprocess.run(
		["freechains", '--host='+hostIp+':'+hostPort, "chain", '#'+str(chainName), 'get', 'block', hash], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def isPost(chainName, hash):
	global hostIp
	global hostPort
	res = getBlockInfo(chainName, hash)
	obj = json.loads(res)
	if obj['sign']:
		if not obj['like']:
			return True
	return False

def listPosts(chainName):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'chain', '#'+str(chainName), 'consensus'], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	posts = freeExec.stdout.split(' ')
	listPosts = []
	for post in posts:
		post = post.replace('\n', '')
		if isPost(chainName, post):
			#repPost = getRepsPost(chainName, post)
			#repPost = repPost.replace('\n', '')
			#if repPost != '-1':
			listPosts.append(post)
	return listPosts

def listBlockedPosts(chainName):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'chain', "#"+str(chainName), 'heads', 'blocked'], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	ps = freeExec.stdout.split(' ')
	listPosts = []
	if ps != ['']:
		for i in ps:
			i = i.replace('\n', '')
			listPosts.append(i)
	return listPosts

def dislikePost(chainName, post, privateKey, msg):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'chain', "#"+str(chainName), 'dislike', post, '--sign=' + privateKey, '--why='+ msg], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def getRepsPost(chainName, post):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'chain', "#"+str(chainName), 'reps', post], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def getRepsUser(chainName, publicKey):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'chain', "#"+str(chainName), 'reps', publicKey], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def sendChainHost(chainName, destIp, destPort):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'peer', destIp+':'+destPort, 'send', "#"+str(chainName)], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def recvChainHost(chainName, origIp, origPort):
	global hostIp
	global hostPort
	freeExec = subprocess.run(
		['freechains', '--host='+hostIp+':'+hostPort, 'peer', origIp+':'+origPort, 'recv', "#"+str(chainName)], capture_output=True, text=True
	)
	if freeExec.stderr:
		print("stderr:", freeExec.stderr)

	return freeExec.stdout

def updatePostList(chainName, newsPosts, posts):
	for newPost in newsPosts:
		exist = False
		p = Post()
		p.setHash(newPost)
		for post in posts:
			if p.getHash() == post.getHash():
				exist = True
				repPost = getRepsPost(chainName, p.getHash())
				repPost = repPost.replace('\n', '')
				if repPost == '-1':
					posts.remove(post)
		if not exist:
			repPost = getRepsPost(chainName, p.getHash())
			repPost = repPost.replace('\n', '')
			p.setReputation(repPost)
			if repPost != '-1':
				posts.append(p)

def updateBlockedPostList(chainName, blockedPosts):
	newBlockedPosts = listBlockedPosts(chainName)
	blockedPosts = []
	for newPost in newBlockedPosts:
		exist = False
		p = Post()
		p.setHash(newPost)
		for post in blockedPosts:
			if p.getHash() == post.getHash():
				exist = True
		if not exist:
			blockedPosts.append(p)
	return blockedPosts

def updateChainsList(chains):
	res = listChain().split(' ')
	if res != ['']:
		for i in res:
			i = i.replace('#', '')
			i = i.replace('\n', '')
			chain = Chain()
			chain.setName(i)
			chains.append(chain)

def print_menu(menuType, posts=None, chainName=None, blockedPosts=None, publicKey=None, reputation=None):
	if menuType == 1:
		print('--------------------------------------------------------------------------------------')
		print('                    Bem vindo ao Forum Só Respostas.\n')
		
		print('Selecione uma opção no menu abaixo:\n')

		print('1 - Entrar com sua senha privada.\n2 - Sair')
	
	if menuType == 2:
		print('--------------------------------------------------------------------------------------')
		print('                    Forum Só Respostas.\n')

		print('User: '+ str(publicKey)+'\n')
		
		print('Selecione uma opção no menu abaixo:\n')
		
		print('1 - Listar disciplinas.\n2 - Ingressar em uma nova disciplina.\n3 - Ingressar em uma disciplina existente.\n4 - Sair da disciplina.\n5 - Voltar ao menu anterior.\n6 - Sair')
	
	if menuType == 3:
		print('--------------------------------------------------------------------------------------')
		print('                    Forum Só Respostas.\n')
		
		print('User: '+ str(publicKey)+' Reps: '+ str(reputation)+'\n')

		print('Disciplina: '+chainName)

		newsPosts = listPosts(chainName)
		updatePostList(chainName, newsPosts, posts)

		print('Posts:\n')
		if posts:
			for post in posts:
				print('File Name: '+str(post.getFileName())+' Hash: '+str(post.getHash())+' Reps: '+ str(post.getReputation())+'\n')
		else:
			print('Sem posts na Disciplina\n')
		
		print('Blocked Posts:\n')
		blockedPosts = updateBlockedPostList(chainName, blockedPosts)

		if blockedPosts:
			for post in blockedPosts:
				print('File Name: '+str(post.getFileName())+' Hash: '+str(post.getHash())+'\n')
		else:
			print('Sem posts bloqueados na Disciplina\n')
	
		print('Selecione uma opção no menu abaixo:\n')
		
		print('1 - Receber novos Post.\n2 - Enviar novos Post.\n3 - Visualizar post.\n4 - Criar novo post.\n5 - Curtir Post.\n6 - Descurtir Post.\n7 - Voltar ao menu anterior.\n8 - Sair')
	
def act1Menu1():
	print('Gerar Par de Chaves\n')

	password = input('Insira sua senha segura: ')
	publicKey,privateKey = newKey(password)

	menuType = 2
	
	return password, privateKey, publicKey, menuType

def act1Menu2(chains):
	#chains = listChain()
	if chains != []:
		print('\nDisciplinas:\n')
		for chain in chains:
			print(chain.getName())
	else:
		print('Não existem Disciplinas disponiveis')

def act2Menu2(publicKey):
	print('\nIngressar em nova Disciplina\n')
	
	chainName = input('Insira o nome da Disciplina: ')
	chain = joinChain(chainName, publicKey)
	menuType = 3
	
	return chain, chainName, menuType

def act3Menu2(chains):
	print('\nIngressar em Disciplina Existente\n')
	exist = False
	chainName = input('Insira o nome da Disciplina: ')
	chain = ''
	for c in chains:
		if chainName == c.getName():
			exist = True
			pionerKey = c.getPionerKey()
	if not exist:
		pionerKey = input('Insira a pioner Key da Disciplina: ')
		chain = joinChain(chainName, pionerKey)
	menuType = 3
	return chain, chainName, menuType, exist, pionerKey

def act4Menu2(chains):
	if chains != []:
		print('\nSair da Disciplina\n')
		chainName = input('Insira o nome da disciplina: ')
		leaveChain(chainName)
		for c in chains:
			if chainName == c.getName():
				chains.remove(c)
				print('Disciplina '+chainName+' Removida.')
	else:
		print('Não existem disciplinas disponiveis')

def act5Menu2():
	menuType = 1
	return menuType

def act1Menu3(chainName):
	print('\nReceber Posts\n')
	
	#hostIp = input('Insira o seu host ip: ')
	#hostPort = input('Insira a porta de execucao: ')
	origIp = input('Insira o host ip de origem: ')
	origPort = input('Insira a porta de execucao de origem: ')
	recvChainHost(chainName, origIp, origPort)

def act2Menu3(chainName):
	print('\nEnviar Posts\n')
	
	#hostIp = input('Insira o seu host ip: ')
	#hostPort = input('Insira a porta de execucao: ')
	destIp = input('Insira o host ip de destino: ')
	destPort = input('Insira a porta de execucao de destino: ')
	sendChainHost(chainName, destIp, destPort)

def act3Menu3(chainName, posts):
	print('\nAcessar Post\n')

	hash = input('Insira o id do post: ')
	outputFile = input('Insira o path de saida do arquivo: ')
	for post in posts:
		exist = False
		if hash == post.getHash():
			exist = True
			res = getPost(chainName, hash, outputFile)
			#print(getPost(chainName, hash, outputFile))
			#post.setReputation(getRepsPost(chainName, hash))
			#print('\nA Reputacao do post é '+str(getRepsPost(chainName, hash)))
			#print('\nA Reputacao do post é '+str(post.getReputation()))
			print('Post Baixado com sucesso.')
	if not exist:
		print('Post não encontrado.')

def act4Menu3(chainName, privateKey, posts, repUser):
	print('\nCriar Post\n')

	post = Post()

	post.setFileName(input('Insira o nome do arquivo: '))
	post.setFilePath(input('Insira o path do arquivo: '))
	post.setPrivateKey(privateKey)
	post.setReputation('0')
	hash = (newPost(chainName, privateKey, post.getFilePath()))
	hash = hash.replace('\n', '')
	post.setHash(hash)
	if hash != '':
		repUser = repUser.replace('\n', '')
		if int(repUser) > 0:
			posts.append(post)
			print('Post adicionado com sucesso')
		else:
			print('Post bloqueado por falta de reputação')


def act5Menu3(chainName, privateKey, posts, blockedPosts):
	print('\nCurtir Post\n')
	
	hash = input('Insira o id do post: ')
	msg = input('Insira o motivo do like: ')
	exist = False
	for post in posts:
		if hash == post.getHash():
			exist = True
			likePost(chainName, hash, privateKey, msg)
	blockedPosts = updateBlockedPostList(chainName, blockedPosts)
	for blockpost in blockedPosts:
		if hash == blockpost.getHash():
			exist = True
			likePost(chainName, hash, privateKey, msg)
	if not exist:
		print('Post não encontrado.')

def act6Menu3(chainName, privateKey, posts):
	print('\nDescurtir Post\n')
	
	hash = input('Insira o id do post: ')
	msg = input('Insira o motivo do dislike: ')
	exist = False
	for post in posts:
		if hash == post.getHash():
			exist = True
			dislikePost(chainName, hash, privateKey, msg)
	if not exist:
		print('Post não encontrado.')

def act7Menu3():
	menuType = 2
	return menuType

def startMenu():
    global user
    global menuType
    global exit	
    while menuType == 1:
        print_menu(menuType)
        selection = input("Sua escolha: ")
        print('--------------------------------------------------------------------------------------')
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
    global chains
    global menuType
    global posts
    global exit
    while menuType == 2:
        print_menu(menuType, publicKey=user.getPublicKey())
        selection = input("Sua escolha: ")
        print('--------------------------------------------------------------------------------------')
        if "1" == selection:
            act1Menu2(chains)
        if "2" == selection:
            hash, chainName, menuType = act2Menu2(user.getPublicKey())
            chain.setName(chainName)
            chain.setHash(hash)
            chain.setPionerKey(user.getPublicKey())
            chains.append(chain)
        if "3" == selection:
            hash, chainName, menuType, exist, pionerKey = act3Menu2(chains)
            chain.setName(chainName)
            if not exist:
                chain.setHash(hash)
                chain.setPionerKey(pionerKey)
                chains.append(chain)
        if "4" == selection:
            act4Menu2(chains)
        if "5" == selection:
            menuType = act5Menu2()
        if "6" == selection:
            exit = True
            return


def postMenu():
    global user
    global chain
    global menuType
    global blockedPosts
    global posts
    global exit
    while menuType == 3:
        user.setReputation(getRepsUser(chainName=chain.getName(), publicKey=user.getPublicKey()))
        print_menu(menuType, posts, chainName=chain.getName(), blockedPosts=blockedPosts, publicKey=user.getPublicKey(), reputation=user.getReputation())
        selection = input("Sua escolha: ")
        print('--------------------------------------------------------------------------------------')
        if "1" == selection:
            act1Menu3(chain.getName())
        if "2" == selection:
            act2Menu3(chain.getName())
        if "3" == selection:
            act3Menu3(chain.getName(), posts)
        if "4" == selection:
            act4Menu3(chain.getName(), user.getPrivateKey(), posts, repUser=user.getReputation())
        if "5" == selection:
            act5Menu3(chain.getName(), user.getPrivateKey(), posts, blockedPosts)
        if "6" == selection:
            act6Menu3(chain.getName(), user.getPrivateKey(), posts)
        if "7" == selection:
            menuType = act7Menu3()
        if "8" == selection:
            exit = True
            return


if __name__ == "__main__":
	freeStart = 0
	hostIp = 'localhost'#input('Insira o seu ip de execucao: ')
	hostPort = input('Insira a porta de execucao: ')
	dirPath = input('Insira o diretorio de execucao: ')
	startHost(hostPort, dirPath)
	print('Esperando o servidor iniciar...')
	time.sleep(5)
	user = User()
	chain = Chain()
	posts = []
	blockedPosts = []
	chains = []
	updateChainsList(chains)
	exit = False
	menuType = 1
	while exit == False:
		if menuType == 1:
			startMenu()
		elif menuType == 2:
			chainMenu()
		elif menuType == 3:
			postMenu()
	if exit:
		freeStart.terminate()
