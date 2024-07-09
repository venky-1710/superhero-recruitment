# Superhero Recruitment System

This project is a web application that predicts whether a superhero should be recruited based on their abilities and performance metrics. It uses machine learning to make predictions and provides a user-friendly interface for input and result display.

## Features

- Input form for superhero attributes
- Machine learning model (Random Forest Classifier) for prediction
- Responsive web design
- Visual feedback on recruitment decision

## Technologies Used

- Python 3.x
- Flask
- NumPy
- Pandas
- Scikit-learn
- HTML/CSS

## Setup and Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/superhero-recruitment.git
```
2. Navigate to the project directory:
```sh
cd superhero-recruitment
```
3. Install the required packages:
```sh
pip install -r requirements.txt
```
4. Run the Flask application:
```sh
python app.py
```
5. Open a web browser and go to `http://localhost:2202` to access the application.

## Usage

1. Fill out the form on the home page with the superhero's attributes:
- Abilities
- Strength (1-10)
- Weaknesses (Yes/No)
- Success Rate (1-100%)
- Missions Completed (0-50)

2. Click "Predict Recruitment" to see the result.

3. The prediction page will show whether the hero is selected or not.

## Data

The model is trained on a dataset (`your_newherodata.csv`) containing superhero information. Ensure this file is present in the `static` folder.

## Model

The application uses a Random Forest Classifier trained on superhero data. The model considers the following features:
- Ability value (encoded)
- Strength
- Weaknesses
- Efficiency (calculated from success rate and missions completed)

## File Structure

- `app.py`: Main Flask application and machine learning model
- `templates/index.html`: Home page with input form
- `templates/predict.html`: Results page
- `static/`: Folder for static files (CSS, images, data)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
