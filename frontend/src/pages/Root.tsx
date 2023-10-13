import React, {useState} from 'react';
import Board from '../components/Board';

const Root: React.FC = () => {
  let [ gameId, setGameId ] = useState<string | null>(null);
  let [ playerId, setPlayerId ] = useState<string | null>(null);
  return (
    <div>
      This is the root!
      <button onClick={() => setGameId("1")}>setGameIdTo1</button>
      <button onClick={() => setPlayerId("2")}>setPlayerIdTo2</button>
      <br/><br/>
      Here is the board
      <br/>
      {gameId && playerId && <Board gameId={gameId} playerId={playerId}/>}
    </div>
  );
}

export default Root;
