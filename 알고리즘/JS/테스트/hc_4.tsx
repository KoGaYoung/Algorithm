// HOC
function withList(ItemComponent) {
  return function WrappedConponent({ items }) {
    return (
      <ul>
        {items.map((item) => (
          <li key={item.text}>
            <ItemComponent item={item} />
          </li>
        ))}
      </ul>
    );
  };
}

const Link = ({ item }) => <a href={item.href}>{item.text}</a>;

const LinkList = withList(Link);

document.body.innerHTML = "<div id='root'></div>";
const rootElement = document.getElementById("root");

if (LinkList) {
  let items = [
    { href: "https://www.google.com", text: "Google" },
    { href: "https://www.bing.com", text: "Bing" },
  ];

  const root = ReactDOM.createRoot(rootElement);

  root.render(<LinkList items={items} />);
  setTimeout(() => {
    console.log(rootElement.innerHTML);
  });
}
