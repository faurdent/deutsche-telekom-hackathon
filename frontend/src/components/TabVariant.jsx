import './TabVariant.css'

function TabVariant({ isActive, text, onClick }) {
    return (
        <button className={"tab-variant " + (isActive ? "tab-variant-active" : "tab-variant-inactive")} onClick={onclick}>
            <p>{ text }</p>
        </button>
    )
}

export default TabVariant