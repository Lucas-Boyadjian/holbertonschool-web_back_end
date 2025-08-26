export default function updateStudentGradeByCity(listStudents, city, newGrades) {
  const listFilter = listStudents.filter((student) => student.location === city);

  const listMap = listFilter.map((student) => {
    const listFind = newGrades.find((grade) => grade.studentId === student.id);

    let finalGrade = 'N/A';
    if (listFind) {
      finalGrade = listFind.grade;
    }

    return {
      ...student,
      grade: finalGrade,
    };
  });
  return listMap;
}
