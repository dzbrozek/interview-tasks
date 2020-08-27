function PromiseAll(promises) {
  // write own implementation of Promise.all
}

PromiseAll([
  1,
  undefined,
  false,
  true,
  [],
  {},
  "foo",
  Promise.resolve(4),
  new Promise(resolve => setTimeout(resolve, 2000, 12345)),
  //new Promise((resolve, reject) => setTimeout(reject, 1000, new Error('boom')))
])
  .then(console.log) // should display all results if last promise commented out
  .catch(console.error); // should display error if last promise uncommented
