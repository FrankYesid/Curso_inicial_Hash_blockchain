# -*- coding: utf-8 -*-
"""
BLOCKCHAIN COMPLETA - SEMANA 2
Implementación educativa de una blockchain funcional en Python

Este archivo contiene el código completo integrado de todos los días de la Semana 2.
Puedes ejecutarlo directamente con: python blockchain_completa.py
"""

import hashlib
import datetime
import json


class Block:
    """
    Clase que representa un bloque individual en la blockchain.
    
    Atributos:
        index (int): Posición del bloque en la cadena
        timestamp (datetime): Marca temporal de creación
        data (str): Información almacenada en el bloque
        previous_hash (str): Hash del bloque anterior
        hash (str): Hash único del bloque actual
    """
    
    def __init__(self, index, data, previous_hash):
        """
        Constructor de la clase Block.
        
        Args:
            index (int): Posición del bloque en la cadena
            data (str): Información almacenada en el bloque
            previous_hash (str): Hash del bloque anterior
        """
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """
        Calcula el hash SHA-256 del bloque.
        
        Returns:
            str: Hash hexadecimal del bloque
        """
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    def is_valid_hash(self):
        """
        Verifica que el hash almacenado sea correcto.
        
        Returns:
            bool: True si el hash es válido, False en caso contrario
        """
        return self.hash == self.calculate_hash()
    
    def to_dict(self):
        """
        Convierte el bloque a un diccionario.
        
        Returns:
            dict: Representación del bloque como diccionario
        """
        return {
            'index': self.index,
            'timestamp': str(self.timestamp),
            'data': self.data,
            'previous_hash': self.previous_hash,
            'hash': self.hash
        }
    
    def __str__(self):
        """
        Representación en string del bloque.
        
        Returns:
            str: Representación legible del bloque
        """
        return f"Block #{self.index} | {self.data} | Hash: {self.hash[:16]}..."


class Blockchain:
    """
    Clase que gestiona la cadena completa de bloques.
    
    Atributos:
        chain (list): Lista de bloques que conforman la blockchain
    """
    
    def __init__(self):
        """
        Constructor de la clase Blockchain.
        Inicializa la cadena con el bloque génesis.
        """
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        """
        Crea el primer bloque de la cadena (bloque génesis).
        
        Returns:
            Block: El bloque génesis
        """
        return Block(0, "Bloque Génesis - Blockchain Educativa", "0")
    
    def get_latest_block(self):
        """
        Obtiene el último bloque de la cadena.
        
        Returns:
            Block: El último bloque de la cadena
        """
        return self.chain[-1]
    
    def add_block(self, data):
        """
        Agrega un nuevo bloque a la cadena.
        
        Args:
            data (str): Información a almacenar en el nuevo bloque
            
        Returns:
            Block: El nuevo bloque agregado
        """
        previous_block = self.get_latest_block()
        new_block = Block(previous_block.index + 1, data, previous_block.hash)
        self.chain.append(new_block)
        return new_block
    
    def get_block(self, index):
        """
        Obtiene un bloque por su índice.
        
        Args:
            index (int): Índice del bloque a obtener
            
        Returns:
            Block: El bloque solicitado, o None si no existe
        """
        if 0 <= index < len(self.chain):
            return self.chain[index]
        return None
    
    def get_chain_length(self):
        """
        Obtiene el número total de bloques en la cadena.
        
        Returns:
            int: Número de bloques
        """
        return len(self.chain)
    
    def is_chain_valid(self):
        """
        Valida la integridad completa de la blockchain.
        
        Returns:
            bool: True si la cadena es válida, False en caso contrario
        """
        # Validar bloque génesis
        if self.chain[0].previous_hash != "0":
            print("ERROR: Bloque genesis invalido")
            return False
        
        # Validar cada bloque
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Verificar hash interno
            if not current_block.is_valid_hash():
                print(f"ERROR: Hash invalido en bloque #{i}")
                return False
            
            # Verificar enlace
            if current_block.previous_hash != previous_block.hash:
                print(f"ERROR: Enlace roto en bloque #{i}")
                return False
            
            # Verificar indice
            if current_block.index != previous_block.index + 1:
                print(f"ERROR: Indice incorrecto en bloque #{i}")
                return False
        
        return True
    
    def find_tampering(self):
        """
        Encuentra bloques que han sido manipulados.
        
        Returns:
            list: Lista de índices de bloques corruptos
        """
        corrupted = []
        
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            if not current.is_valid_hash():
                corrupted.append(i)
            elif current.previous_hash != previous.hash:
                corrupted.append(i)
        
        return corrupted
    
    def display_chain(self):
        """
        Muestra la cadena completa de bloques en la consola.
        """
        print("\n" + "=" * 70)
        print("BLOCKCHAIN COMPLETA".center(70))
        print("=" * 70)
        for block in self.chain:
            print(f"  {block}")
        print("=" * 70)
        print(f"Total de bloques: {len(self.chain)}")
        print(f"Blockchain valida: {'SI' if self.is_chain_valid() else 'NO'}")
        print("=" * 70 + "\n")
    
    def to_json(self):
        """
        Convierte la blockchain completa a formato JSON.
        
        Returns:
            str: Representación JSON de la blockchain
        """
        return json.dumps([block.to_dict() for block in self.chain], indent=2)


def demo_blockchain():
    """
    Función de demostración que muestra el uso completo de la blockchain.
    """
    print("\n" + "#" * 70)
    print("DEMOSTRACIÓN: BLOCKCHAIN FUNCIONAL EN PYTHON".center(70))
    print("#" * 70 + "\n")
    
    # Crear blockchain
    print(">> Creando blockchain...")
    mi_blockchain = Blockchain()
    print(f"   Blockchain creada con {mi_blockchain.get_chain_length()} bloque (genesis)\n")
    
    # Agregar transacciones
    print(">> Agregando transacciones...")
    mi_blockchain.add_block("Alice envia 50 BTC a Bob")
    print("   Bloque #1 agregado")
    
    mi_blockchain.add_block("Bob envia 20 BTC a Charlie")
    print("   Bloque #2 agregado")
    
    mi_blockchain.add_block("Charlie envia 10 BTC a Diana")
    print("   Bloque #3 agregado")
    
    mi_blockchain.add_block("Diana envia 5 BTC a Alice")
    print("   Bloque #4 agregado\n")
    
    # Mostrar blockchain
    mi_blockchain.display_chain()
    
    # Demostrar inmutabilidad
    print(">> DEMOSTRACION DE INMUTABILIDAD")
    print("=" * 70)
    print("Intentando corromper el bloque #2...")
    print(f"Dato original: {mi_blockchain.chain[2].data}")
    
    # Modificar datos
    mi_blockchain.chain[2].data = "Bob envia 100 BTC a Charlie (MODIFICADO ILEGALMENTE)"
    print(f"Dato modificado: {mi_blockchain.chain[2].data}")
    
    # Validar
    print(f"\nBlockchain valida despues de la modificacion? ", end="")
    if mi_blockchain.is_chain_valid():
        print("SI (esto no deberia pasar)")
    else:
        print("NO (Manipulacion detectada!)")
    
    # Encontrar bloques corruptos
    corrupted = mi_blockchain.find_tampering()
    if corrupted:
        print(f"Bloques corruptos detectados: {corrupted}")
    
    print("=" * 70 + "\n")
    
    # Crear blockchain limpia para exportar
    print(">> EXPORTACION A JSON")
    print("=" * 70)
    blockchain_limpia = Blockchain()
    blockchain_limpia.add_block("Transaccion 1")
    blockchain_limpia.add_block("Transaccion 2")
    blockchain_limpia.add_block("Transaccion 3")
    
    json_output = blockchain_limpia.to_json()
    print("Blockchain exportada a JSON:")
    print(json_output[:500] + "..." if len(json_output) > 500 else json_output)
    print("=" * 70 + "\n")
    
    # Conclusion
    print("#" * 70)
    print("DEMOSTRACION COMPLETADA".center(70))
    print("#" * 70)
    print("\n>> Has visto una blockchain funcional en accion.")
    print(">> Conceptos demostrados:")
    print("   - Creacion de bloques")
    print("   - Enlace criptografico")
    print("   - Validacion de integridad")
    print("   - Deteccion de manipulaciones")
    print("   - Inmutabilidad\n")


if __name__ == "__main__":
    # Ejecutar demostracion
    demo_blockchain()
    
    # Opcion interactiva
    print("\n" + "=" * 70)
    print("MODO INTERACTIVO")
    print("=" * 70)
    print("\nQuieres crear tu propia blockchain? (s/n): ", end="")
    
    try:
        respuesta = input().lower()
        
        if respuesta == 's':
            print("\n>> Creando tu blockchain personalizada...\n")
            mi_bc = Blockchain()
            
            while True:
                print("\nOpciones:")
                print("1. Agregar bloque")
                print("2. Ver blockchain")
                print("3. Validar blockchain")
                print("4. Salir")
                print("\nElige una opcion (1-4): ", end="")
                
                opcion = input()
                
                if opcion == "1":
                    print("Ingresa los datos del bloque: ", end="")
                    datos = input()
                    mi_bc.add_block(datos)
                    print(f"   Bloque #{mi_bc.get_chain_length() - 1} agregado")
                
                elif opcion == "2":
                    mi_bc.display_chain()
                
                elif opcion == "3":
                    if mi_bc.is_chain_valid():
                        print("   Blockchain valida")
                    else:
                        print("   Blockchain corrupta")
                
                elif opcion == "4":
                    print("\nHasta luego!\n")
                    break
                
                else:
                    print("Opcion invalida")
        
        else:
            print("\nHasta luego!\n")
    
    except KeyboardInterrupt:
        print("\n\nHasta luego!\n")
    except EOFError:
        print("\n\nHasta luego!\n")
