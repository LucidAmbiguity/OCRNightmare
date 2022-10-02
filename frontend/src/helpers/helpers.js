export const EndPoints = {
  LOGIN: 'http://localhost:5000/auth/login',
  REGISTER: 'http://localhost:5000/auth/register',
  AUTHOR: 'http://localhost:5000/author',
  AUTHORS: 'http://localhost:5000/authors',
  TOKEN_CHECK: 'http://localhost:5000/auth/check_token',
};

export const APIPoints = {
  PROJECT: 'http://localhost:5000/ocrnightmare/projects',
  FORMS: 'http://localhost:5000/ocrnightmare/forms',
  REGISTER: 'http://localhost:5000/auth/register',
  AUTHOR: 'http://localhost:5000/author',
  AUTHORS: 'http://localhost:5000/authors',
  TOKEN_CHECK: 'http://localhost:5000/auth/check_token',
};

export const projDataCheck = (projData) => {
  const results = projData.map((page, i) => {
    if (!page.data) return false;
    if (!page.data) return false;
    console.log('page.data.length', page.data.length);
    if (page.data.length < 1) return false;
    return true;
  });
  // # Return TRUE if no false in results.
  return !results.includes(false);
};

// export const projGetSamplesDataCheck = (projSampHeaders) => {
//   const results = projSampHeaders.map((page, i) => {
//     if (!page.data) return false;
//     if (!page.data) return false;
//     if (page.data.length < 1) return false;
//     return true;
//   });
//   // # Return TRUE if no false in results.
//   return !results.includes(false);
// };

export const getInitialStateColumnIndexForm = (pagesColIdx) => {
  const InitSt = {};
  pagesColIdx.forEach((set, idxa) => {
    const temp = Array.from(set).sort((a, b) => a - b);
    temp.forEach((index, idxb) => {
      InitSt[`index-${idxa}-${idxb}`] = index;
    });
  });
  return InitSt;
};

// export enum EndPoints{
//   LOGIN = "http://localhost:5000/apiocr/login",
//   REGISTER = "http://localhost:5000/apiocr/register",
//   AUTHOR = "http://localhost:5000/apiocr/author",
//   AUTHORS = "http://localhost:5000/apiocr/authors",
//   TOKEN_CHECK = "http://localhost:5000/apiocr/check_token",
// }
// export enum EndPoints{
//   LOGIN = "http://192.168.1.3:5000/login",
//   REGISTER = "http://192.168.1.3:5000/register",
//   AUTHOR = "http://192.168.1.3:5000/author",
//   AUTHORS = "http://192.168.1.3:5000/authors",
//   TOKEN_CHECK = "http://192.168.1.3:5000/check_token",
// }
