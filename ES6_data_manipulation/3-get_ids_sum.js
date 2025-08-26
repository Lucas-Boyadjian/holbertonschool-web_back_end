export default function getStudentIdsSum(listStudents) {
  if (!Array.isArray(listStudents)) return [];
  return listStudents.reduce((acc, listStudents) => acc + listStudents.id, 0);
}
