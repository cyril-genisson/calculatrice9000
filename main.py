#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Project: Calculatrice 9000
# Filename: main.py
# Created: 28/11/2023
#
# Licence: GPLv3
#
# Author: Cyril GENISSON
import ast
import operator as op

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}


def eval_expr(expr):
    return eval_(ast.parse(expr, mode='eval').body)


def eval_(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)


def menu():
    print('\n')
    print("Choix 1: nouveau calcul")
    print("Choix 2: afficher l'historique des calculs")
    print("Choix 3: supprimer l'historique")
    print("Choix 4: sortir du programme")


if __name__ == "__main__":
    history = []
    print(80 * "*")
    print( 3 * '\t' + "Calculatrice 9000")
    print(80 * "*")
    while True:
        menu()
        opt = input("Choisir votre option: ")
        match opt:
            case '1':
                exp = input("\nNouveau calcul: ")
                try:
                    res = eval_expr(exp)
                except:
                    print("Expression incorrect")
                    res = "Erreur"
                finally:
                    print(f"Résultat: {res}")
                    print()
                    history.append((exp, res))
            
            case '2':
                print('\n' + 80 * '*')
                print('\t' * 3 + "Historique des calculs")
                print( 80 * '*')
                print('\n')
                header = ("Id","Résultat", "Expression calculée")
                print(f"{header[0]: ^5}|{header[1]: ^35}|{header[2]: ^35}")
                print(80 * '-')
                for k in range(len(history)):
                    print(f"{k+1: ^5}|{history[k][1]: ^35}|{history[k][0]: ^35}")

            case '3':
                print('\n' + 80 * '*')
                print('\t' * 3 + "Suppression de l'historique")
                print( 80 * '*')
                history = []
            
            case '4':
                print("Fin du programme...")
                exit(0)
            
            case _:
                print("Option inconnue")
