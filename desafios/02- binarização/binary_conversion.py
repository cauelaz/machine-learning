from PIL import Image

# Carrega a imagem colorida
imagem = Image.open("imagem.jpg").convert("RGB")

largura, altura = imagem.size

# Cria as imagens de saída
imagem_cinza = Image.new("L", (largura, altura))
imagem_binaria = Image.new("L", (largura, altura))

# Limiar utilizado na binarização
limiar = 128

for y in range(altura):
    for x in range(largura):

        # Obtém os valores RGB do pixel
        r, g, b = imagem.getpixel((x, y))

        # Converte RGB para nível de cinza
        # Utilizamos pesos diferentes devido à percepção humana das cores
        cinza = int(
            0.299 * r +
            0.587 * g +
            0.114 * b
        )

        # Salva o pixel na imagem em escala de cinza
        imagem_cinza.putpixel((x, y), cinza)

        # Binarização
        if cinza >= limiar:
            binario = 255  # Branco
        else:
            binario = 0    # Preto

        imagem_binaria.putpixel((x, y), binario)

# Salva os resultados
imagem_cinza.save("imagem_cinza.jpg")
imagem_binaria.save("imagem_binaria.jpg")

# Exibe as imagens
imagem.show()
imagem_cinza.show()
imagem_binaria.show()