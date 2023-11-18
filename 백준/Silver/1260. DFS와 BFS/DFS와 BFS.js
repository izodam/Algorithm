const fs = require('fs');
// const input = fs.readFileSync('example.txt').toString().trim().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = +input[0].split(' ')[0];
const m = +input[0].split(' ')[1];
const v = +input[0].split(' ')[2];

const graph = Array.from({length: (n+1)}, () => Array.from({length: (n+1)}, () => 0));

for(let i = 1; i <= m; i++){
    let s = +input[i].split(' ')[0];
    let e = +input[i].split(' ')[1];

    graph[s][e] = 1;
    graph[e][s] = 1;
}

const dfsVisit = Array.from({length: (n+1)}, () => 0);
const bfsVisit = Array.from({length: (n+1)}, () => 0);

const dfsRes = [];
const bfsRes = [];

function dfs(v){
    if (dfsVisit[v])    return;
    dfsVisit[v] = 1;
    dfsRes.push(v);
    for (let i = 0; i < graph[v].length; i++){
        if (!dfsVisit[i] && graph[v][i] == 1){
            dfs(i);
        }
    }
}

function bfs(v){
    let q = [v];
    bfsVisit[v] = 1;
    
    while (q.length){
        let x = q.shift();
        bfsRes.push(x);
        for(let i = 0; i < graph[x].length; i++){
            if(!bfsVisit[i] && graph[x][i] == 1){
                q.push(i);
                bfsVisit[i] = 1;
            }
        }
    }
}

dfs(v)
bfs(v)
console.log(dfsRes.join(' '))
console.log(bfsRes.join(' '))