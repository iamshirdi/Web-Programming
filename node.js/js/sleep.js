function sleep(ms) {
  console.log('i am sleeping log')
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}


async function main() {
  console.log(1);
  await sleep(5000);
  console.log(2);
}
main()
