export default function createReportObject(employeesList) {
  return {

    allEmployees: { ...employeesList },
    getNumberOfDepartments(args) {
      return Object.keys(args).length;
    },
  };
}
