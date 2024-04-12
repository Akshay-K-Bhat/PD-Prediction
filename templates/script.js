const inputs = document.querySelectorAll('input');

let arr = [4.21158027e-01, -8.43909404e-01, -7.54129606e-01,
    -8.18181818e-01, -8.30443160e-01, -8.18863880e-01,
    -8.30791459e-01, -8.59229505e-01, -8.52095316e-01,
    -8.83667180e-01, -8.91180461e-01, -8.57110039e-01,
    -8.83682116e-01, -8.89422924e-01, 4.02015769e-01,
    7.40933452e-02, -1.89334120e-01, 2.17565942e-01,
    6.47115499e-01, 3.81399620e-01, -1.31433968e-02];
let index = 0;
inputs.forEach((input) => {
    input.value = arr[index];
    index += 1;
});

// Define the URL of your Flask application
const url = 'http://127.0.0.1:5000/predict';  // Update this URL with your actual server address

// Define the data you want to send in the POST request
const data = new FormData();
data.append('input1', 'value1'); 
data.append('input2', 'value2');
data.append('input3', 'value3');
data.append('input4', 'value4');
data.append('input5', 'value5');
data.append('input6', 'value6');
data.append('input7', 'value7');
data.append('input8', 'value8');
data.append('input9', 'value9');
data.append('input10', 'value10');
data.append('input11', 'value11');   
data.append('input12', 'value12');
data.append('input13', 'value13');
data.append('input14', 'value14');
data.append('input1', 'value1');
data.append('input1', 'value1');
data.append('input1', 'value1');
data.append('input1', 'value1');
data.append('input1', 'value1');
data.append('input1', 'value1');
data.append('input1', 'value1');
// Add more key-value pairs for other input fields as needed

// Send the POST request using fetch
fetch(url, {
    method: 'POST',
    body: data
})
    .then(response => {
        if (response.ok) {
            console.log('POST request was successful!');
        } else {
            console.error('Error:', response.status);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });


<script>
    const inputs = document.querySelectorAll('input');

    let arr = [4.21158027e-01, -8.43909404e-01, -7.54129606e-01,
    -8.18181818e-01, -8.30443160e-01, -8.18863880e-01,
    -8.30791459e-01, -8.59229505e-01, -8.52095316e-01,
    -8.83667180e-01, -8.91180461e-01, -8.57110039e-01,
    -8.83682116e-01, -8.89422924e-01, 4.02015769e-01,
    7.40933452e-02, -1.89334120e-01, 2.17565942e-01,
    6.47115499e-01, 3.81399620e-01, -1.31433968e-02];
    let index = 0;
        inputs.forEach((input) => {
        input.value = arr[index];
    index += 1;
        });

    document.addEventListener('DOMContentLoaded', function () {
            const form = document.querySelector('form');

    // Event listener for form submission
    form.addEventListener('submit', function (event) {
        event.preventDefault();  // Prevent the default form submission

    const formData = new FormData(form);
    // Define the URL of your Flask application
    const url = 'http://127.0.0.1:5000/predict';

    // Send the POST request using fetch
    fetch(url, {
        method: 'POST',
    body: formData
                })
                    .then(response => {
                        if (response.ok) {
        console.log(response);
                        } else {
        console.error('Error:', response.status);
                        }
                    })
                    .catch(error => {
        console.error('Error:', error);
                    });
            });
        });

</script>