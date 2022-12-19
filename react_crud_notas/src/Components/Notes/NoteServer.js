const API_URL = "127.0.0.1:8000/api/notas/";

export const listNotas = async () => {
    return await fetch(API_URL)
};