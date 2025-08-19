export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;
  
  if (trueOrFalse) {
    // Variables are not overwritten in this block.
  }

  return [task, task2];
}
