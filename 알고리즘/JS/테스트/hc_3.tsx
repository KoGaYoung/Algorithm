/**
 * input fields component
 */
const ContactForm = () => {
  // 성, 이름, 이메일
  const [formData, setFromData] = React.useState({
    firstName: "",
    age: 0,
    email: "",
  });

  /**
   * typescript 적용 전 타입 표기
   * @parma (e) React.ChangeEvent<HTMLInputElement>
   */
  const handleInputChange = (e) => {
    const { name, value } = e.target;

    setFromData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <div>
      {/* use label than placeHolder becuase of UX */}
      <div class="firstName">
        <label for="firstName">firstName</label>
        <input
          type="text"
          name="firstName"
          value={formData.firstName}
          onChange={handleInputChange}
        />
      </div>

      <div class="age">
        <label for="age">age</label>
        <input
          type="number"
          name="age"
          value={formData.age}
          onChange={handleInputChange}
        />
      </div>

      {formData.age >= 14 && (
        <div class="email">
          <label for="email">email</label>
          <input
            type="text"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
          />
        </div>
      )}
    </div>
  );
};

document.body.innerHTML = "<div id='root'></div>";
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<ContactForm />);
