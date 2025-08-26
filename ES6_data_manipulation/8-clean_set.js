export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }
  const strArray = [];
  for (const element of set) {
    if (element.startsWith(startString)) strArray.push(element.slice(startString.length));
  }
  return strArray.join('-');
}
