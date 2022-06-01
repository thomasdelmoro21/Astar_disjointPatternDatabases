# Astar_disjointPatternDatabases
### Main
Il modulo main.py contiente tutti i test effettuati e il codice per la generazione dei risultati. Per eseguire i test impostare la variabile numOfTests a un valore arbitrario, è consigliato un numero di test tra i 10 e i 100 per ottenere risultati significativi. La variabile N può essere impostata a valore 15 per eseguire i test sul 15-puzzle e a valore 8 per l'8-puzzle. Il codice non è ottimizzato per gestire il 15-puzzle, quindi è consigliato impostare N=8 per eseguire i test in tempi ragionevoli.
Il metodo shuffle in main.py serve a creare una disposizione iniziale casuale, è possibile cambiare il numero di mosse da fare ma è consigliato usare un numero random maggiore di 100 per avere dei tempi di esecuzione leggibili.
### ManhattanDistance
Questo modulo contiene il codice per eseguire il calcolo della distanza Manhattan su un nodo in input
### LinearConflicts
Il metodo linearConflicts è chiamato dal solver per calcolare il valore dell'euristica Linear Conflicts su un nodo in input
### NonAdditive
Questo modulo contiene il codice per l'euristica Non Additive Database. Il metodo generateNonAdditiveDatabase() è chiamato nel main.py per generare i database, mentre il nonAdditiveCost() è il metodo chiamato a ogni iterazione dal solver.
### DisjointDatabases
Il modulo contiene il codice per l'utilizzo dell'euristica Disjoint Pattern Databases. In particolare il metodo generateDisjointDatabases() è chiamato in main.py per generare i database prima dell'esecuzione. Al contrario disjointCost() è usato dal solver per ottenere il valore dell'euristica corrispondente a un certo nodo.
### ReflectedDatabases
Questo modulo contiene il codice per generare il Reflected Databases. Il solver ad ogni iterazione chiamerà sia disjointCost() che reflectedCost() e prenderà il valore maggiore ritornato.
