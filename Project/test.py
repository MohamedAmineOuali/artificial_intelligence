import Algorithms



NAME="NAME"
NODE1="NODE1"
NODE2="NODE2"
VAL="LENGTH"
from Graph import  *


GRAPH1 = Graph(edgesdict = \
               [{NAME:'e1',  VAL: 5, NODE1:'1', NODE2:'2'},
                {NAME:'e2',  VAL:15, NODE1:'3', NODE2:'4'},
                {NAME:'e3',  VAL: 7, NODE1:'5', NODE2:'4'},
                {NAME:'e4',  VAL:25, NODE1:'6', NODE2:'9'},
                {NAME:'e5',  VAL: 5, NODE1:'8', NODE2:'10'},
                {NAME:'e6',  VAL: 3, NODE1:'11', NODE2:'13'},
                {NAME:'e7',  VAL: 1, NODE1:'7', NODE2:'3'},
                {NAME:'e8',  VAL: 4, NODE1:'14', NODE2:'6'},
                {NAME:'e9',  VAL: 2, NODE1:'2', NODE2:'7'},
                {NAME:'e10', VAL: 9, NODE1:'13', NODE2:'2'},
                {NAME:'e11', VAL: 6, NODE1:'3', NODE2:'6'},
                {NAME:'e12', VAL: 4, NODE1:'8', NODE2:'2'},
                {NAME:'e13', VAL:10, NODE1:'5', NODE2:'3'},
                {NAME:'e14', VAL: 5, NODE1:'10', NODE2:'2'},
                {NAME:'e15', VAL: 8, NODE1:'2', NODE2:'11'},
                {NAME:'e16', VAL: 3, NODE1:'3', NODE2:'2'},
                {NAME:'e17', VAL: 8, NODE1:'12', NODE2:'1'}
                ],
               heuristic = \
               {'14':
                    {'4':17,
                     '5':10,
                     '3':7,
                     '6':13,
                     '14':15,
                     '9':14,
                     '8':8,
                     '10':6,
                     '2':4,
                     '7':6,
                     '1':0,
                     '13':12,
                     '11':1000,
                     '12':6 }})


#GRAPH1.display([12])
print(Algorithms.a_star(GRAPH1,'1','14'))
