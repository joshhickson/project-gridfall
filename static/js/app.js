document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/history')
        .then(response => response.json())
        .then(data => {
            const labels = data.map(item => new Date(item.timestamp).toLocaleString());
            const medianData = data.map(item => item.forecast.median_collapse_week);

            const ctx = document.getElementById('forecastChart').getContext('2d');
            const forecastChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Median Collapse Week Forecast',
                        data: medianData,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1,
                        tension: 0.1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Forecasted Collapse Week'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Date of Forecast'
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching simulation history:', error));
});
