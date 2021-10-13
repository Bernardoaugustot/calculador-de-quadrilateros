'''
    Classe retângulo
    Quando um objeto Rectangle é criado, ele deve ser inicializado com os atributos widthe height. A classe também deve conter os seguintes métodos:

    set_width
    set_height
    get_area: Área de devoluções ( width * height)
    get_perimeter: Retorna o perímetro ( 2 * width + 2 * height)
    get_diagonal: Retorna diagonal ( (width ** 2 + height ** 2) ** .5)
    get_picture: Retorna uma string que representa a forma usando linhas de " * ".
     O número de linhas deve ser igual à altura e o número de " * " em cada linha deve ser igual à largura.
     Deve haver uma nova linha ( \n) no final de cada linha. Se a largura ou altura for maior que 50, isso deve retornar a string: "Muito grande para a imagem.".
    get_amount_inside: Assume outra forma (quadrado ou retângulo) como argumento. Retorna o número de vezes que a forma passada caberia dentro da forma (sem rotações). Por exemplo, um retângulo com largura 4 e altura 8 pode caber em dois quadrados com lados de 4.
    Além disso, se uma instância de um retângulo for representada como uma string, deve ser semelhante a: Rectangle(width=5, height=10)

    Classe quadrada
    A classe Square deve ser uma subclasse de Rectangle. Quando um objeto Square é criado, um único comprimento de lado é passado.
     O __init__método deve armazenar o comprimento do lado nos atributos widthe heightda classe Rectangle.
        A classe Square deve ser capaz de acessar os métodos da classe Rectangle, mas também deve conter um set_sidemétodo.
         Se uma instância de um Square é representada como uma string, deve ser semelhante a:Square(side=9)
        Além disso, os métodos set_widthe set_heightna classe Square devem definir a largura e a altura.
        '''
class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def set_width(self, width): #Definir largura
        self.width = width
    def set_height(self, height): #Definir Altura
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return (self.width *2)+(self.height *2)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def __str__(self):
        return "Rectangle(width="+str(self.width) +", height="+ str(self.height)+ ")"
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        texto = ""
        for x in range(self.height):
            for Y in range(self.width):
                texto += "*"
            texto = texto + "\n"
        return texto
    def get_amount_inside(self, forma):
        #x3 = (forma.width * forma.width) / (self.width * self.height)
        print("Lados da forma original (H/W) "+str(self.height) +"  "+ str(self.width))
        print("Lados da forma Recebida (H/W) "+str(forma.height)+ "  " + str(forma.width))
        cH =  self.height /forma.height 
        cW =  self.width / forma.width 
        print("Resultado: "+str(int(cH * cW)))
        return int(cH * cW)

class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.height = width
    def get_picture(self):
        texto = ""
        for x in range(self.height):
            for Y in range(self.width):
                texto += "*"
            texto = texto + "\n"
        return texto
    def set_side(self, side):
        self.width = side
        self.height = side
    def __str__(self):
        return "Square(side="+str(self.width) + ")"

'''
print("Strat")

rect = Rectangle(5, 10)
#print(rect.get_area())
rect.set_width(3)
#print(rect.get_perimeter())
#print(rect)

sq = Square(9)
#print(sq.get_area())
sq.set_side(4)
#print(sq.get_diagonal())
#print(sq)

rect2 = Rectangle(4, 8)
print(rect2.get_amount_inside(rect))
print("End")
'''







