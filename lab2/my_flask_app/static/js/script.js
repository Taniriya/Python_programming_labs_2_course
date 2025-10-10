document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#addUserForm').addEventListener('submit', async (event) => {
        event.preventDefault(); // Предотвращаем стандартную отправку формы

        const formData = new FormData(event.target); // Данные формы

        try {
            const response = await fetch('/add_user', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                window.location.href = '/users'; // Переходим на страницу с пользователями
            } else {
                alert('Ошибка при сохранении пользователя.');
            }
        } catch (err) {
            console.error(err);
            alert('Возникла ошибка сети.');
        }
    });
});