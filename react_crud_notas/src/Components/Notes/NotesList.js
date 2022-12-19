import React, { useEffect, useState } from "react";
import * as NoteServer from "./NoteServer";

const NoteList = () => {

    const [notas, setnotas] = useState([]);

    const listNotas = async() => {
        try{
            const res = await NoteServer.listNotas();
            const data = await res.json();
            setnotas(data.notas);
            console.log(data);
        }   catch(error) {
            console.log(error);
        }
    };

    useEffect(() => {
        listNotas();
    }, []);

    return (
        <div>
            {notas.map((nota) => (
                <h2>{nota.name}</h2>
            ))}
        </div>
    );
};

export default NoteList;