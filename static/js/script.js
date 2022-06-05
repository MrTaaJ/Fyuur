window.parseISOString = function parseISOString(s) {
  var b = s.split(/\D+/);
  return new Date(Date.UTC(b[0], --b[1], b[2], b[3], b[4], b[5], b[6]));
};

const venueSearch = document.getElementById('venue-search')
venueSearch.addEventListener("submit", function (event) {
  // event.preventDefault()
  console.log(document.querySelector('.venue-search').value)
  fetch('/venues/search', {
      method: 'POST',
      body: JSON.stringify({
        'search': document.querySelector('.venue-search').value
      }),
      headers: {
        'Content-Type': 'application/json'
      }
  })
})