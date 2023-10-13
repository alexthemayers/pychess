import React, { useState } from 'react';
import axios, { AxiosError, AxiosResponse } from 'axios';
import { config } from "../config";
interface BoardProps {
  playerId: string
  gameId: string
}

const Board:React.FC<BoardProps> = ({playerId, gameId}): React.JSX.Element => {
  const [data, setData]: [string | null, React.Dispatch<React.SetStateAction<string | null>>] = useState<string | null>(null);
  const [error, setError]: [string | null, React.Dispatch<React.SetStateAction<string | null>>] = useState<string | null>(null);

  // const boardUrl = config.basePath
  const catFactUrl: string = "https://catfact.ninja/fact"
  const fetchData = async (): Promise<void> => {
    try {
      const response : AxiosResponse<string> = await axios.get<string>(catFactUrl);
      setData(response.data);
    } catch (err: unknown) {
      console.log(typeof(err));
      console.error(err);
      if (isAxiosError(err)) {
        if (err.response && err.response.status === 404) setError('Error: Resource not found (404)');
      } else {
        setError(`An error occurred while fetching data. ${err}`);
      }
    }
  };

  return (
    <div>
      GameId: {gameId}
      <br/>
      PlayerId: {playerId}
      <br/>
      <button onClick={fetchData}>Fetch Data</button>
      {data && (
        <div>
          <h2>Successful Response:</h2>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}
      {error && (
        <div>
          <h2>Error:</h2>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
};

function isAxiosError(error: unknown): error is AxiosError {
  return (error as AxiosError).isAxiosError;
}
export default Board;
