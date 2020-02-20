let defaultnote=" The event binding allows you to add an event handler for a specified event so that your chosen JavaScript function will be invoked when that event is triggered for the associated DOM element. This can be used to bind to any event, such as keypress, mouseover or mouseout. "
let bingdict="https://cn.bing.com/dict/search?q=";
let ydict="http://dict.youdao.com/w/"
let ydcollinsid="#authTrans"
//http://m.youdao.com/dict?le=eng&q=game#collins
let notes=[
    {
        'id':0,
        'content':"this is first note",
        'user_id': 0
    },
    {
        'id':1,
        'content': "this is second note",
        'user_id': 0
    },
    {
        'id':2,
        'content':"this third note",
        'user_id': 1
    }
]

class Note{
    constructor(note_data){
        this.id=ko.observable(note_data.id);
        this.content=ko.observable(note_data.content);
        this.user_id=ko.observable(note_data.user_id);
        this.state=ko.observable('small');

        this.width=ko.observable(30);
        this.height=ko.observable(this.width()/2);
        this.state=ko.observable('small');
    };
    
    zoom(){
        if(this.state()==='small'){
            this.state('large');
            this.width(this.width()*2);
            this.height(this.height()*2);
        }
        else if(this.state()==='large'){
            this.state('small');
            this.width(this.width()/2);
            this.height(this.height()/2)
        }
        else{
            this.state('small');
        }
    }
}

class Dict{
    
    constructor(src){
        this.src=ko.observable(src);
        this.display=ko.observable('none')
    }
    lookup(){
        //if dict is displayed on page close it 
        if(this.display()=='initial'){
            this.display('none');
            return;
        }
        let word=window.getSelection().toString();
        this.display("initial")
        this.src(ydict+word+ydcollinsid) //i.src="https://cn.bing.com/dict/search?q=root"        
    }
    close(){
        this.display("none")
    }
}

function ViewModel(){
  let self=this;
  
  self.dict=ko.observable(new Dict(""))
  self.lookup=function (event) {
      console.log('lookup')
      self.dict().lookup();
  }
  self.closedict=function (event) {
      console.log(self.dict().display())
      let cdict=self.dict();
      cdict.close();
      console.log(self.dict().display())
  }
  

  self.noteList=ko.observableArray([]);
  for (const note of notes) {
      self.noteList().push(new Note(note));
  }
  
}

ko.applyBindings(new ViewModel())