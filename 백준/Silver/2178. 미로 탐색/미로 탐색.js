const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// '/dev/stdin'

const n = +input[0].split(' ')[0];
const m = +input[0].split(' ')[1];

const graph = [];
for(let i = 0; i < n; i++){
    graph.push(input[i+1].split('').map(Number));
}

const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

function bfs(a,b){
    const q = [[0,0]];
    
    while(q.length){
        let [x,y] = q.shift();

        for(let i = 0; i < 4; i++){
            let nx = x + dx[i];
            let ny = y + dy[i];
            if(nx<0 || nx>=n || ny<0 || ny>=m)  continue;
            if(graph[nx][ny] === 1){
                q.push([nx,ny]);
                graph[nx][ny] = graph[x][y] + 1;
            }
        }
    }

    return graph[a][b];
}

console.log(bfs(n-1,m-1));