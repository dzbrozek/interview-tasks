function fetchMock(response, delay) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if(response instanceof Error) {
        reject(response);
      } else {
        resolve(response);
      }
    }, delay);
  });
}

fetchMock({
  id: 1,
  name: 'John Smith'
}, 2000)
  .then(console.log);

fetchMock(new Error('bing bang'), 2000)
  .catch(console.error);
