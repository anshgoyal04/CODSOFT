document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault();
    // Perform signup process
    // You can add your signup logic here, such as sending data to a server
    alert('Sign up successful! Redirecting to home page...');
    // Redirect to home page after successful signup
    window.location.href = 'home.html';
});
