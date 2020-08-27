function fetchMock(response, delay) {
  // return response after given delay
}

fetchMock({
  id: 1,
  name: 'John Smith'
}, 2000)
  .then(console.log);

fetchMock(new Error('bing bang'), 2000)
  .catch(console.error);
