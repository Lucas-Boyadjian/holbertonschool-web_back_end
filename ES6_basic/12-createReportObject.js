export default function createReportObject(employeesList) {

  let departmentNames = Object.keys(employeesList);

  return {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      return Object.keys(employeesList).length;
    },
  };
}
