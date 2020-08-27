function PromiseAll(promises) {
	return new Promise((resolve, reject) => {
  	const results = new Array(promises.length);
    let numResults = 0;
    
    if(!promises.length) {
    	resolve(results);
    }
  
  	promises.forEach((promise, index) => {
  		Promise.resolve(promise).then((response) => {
      	results[index] = response;
        numResults++;
        
        if(numResults === promises.length) {
        	resolve(results);
        }
      }).catch((error) => {
      	reject(error);
      });
  	});
  });
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
  .then(console.log)
  .catch(console.error);
