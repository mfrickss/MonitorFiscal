import './Card.css'

function Card(props) {
    return (
        <div className="card-cotacao">
            <h3>{props.titulo}</h3>
            <div className="valor">R$ {props.valor}</div>
            <p className="rodape">Atualizado agora!</p>
        </div>
    )
}

export default Card