#include<iostream>
#include<stdio.h>
#include<windows.h>

using namespace std;

#define red 0
#define black 1

struct node{
	node* parent;
	node* left;
	node* right;
	int color;
	int value;
};

//insert函数族
void insert_case1(node* N);
void insert_case2(node* N);
void insert_case3(node* N);
void insert_case4(node* N);
void insert_case5(node* N);

//delete函数族
void delete_one_child(node* N);
void delete_case1(node* N);
void delete_case2(node* N);
void delete_case3(node* N);
void delete_case4(node* N);
void delete_case5(node* N);
void delete_case6(node* N);


//定义输出时需要的几个特殊节点
node* root;
node* left;
node* right;

//记录插入节点数量
int num=0;

//定义插入树函数
void insert(){
	node* insert_fore;
	//node* insert_behind;
	node* new_node;
	int value = 0;
	if(num == 0){
		root = new node;
		cout<<"请输入第一个节点值："<<endl;
		cin>>value;
		root->value = value;
		root->parent = NULL;
		root->left =NULL;
		root->right = NULL;
		root->color = red;
		num++;
		new_node = root;
	}
	else{
		cout<<"请输入节点值："<<endl;
		cin>>value;
		insert_fore=root;
		while(insert_fore != NULL){
			//insert_behind = insert_fore;
			if(value > insert_fore->value){
				if(insert_fore->right == NULL){
					new_node = new node;
					new_node->color = red;
					new_node->value = value;
					insert_fore->right = new_node;
					new_node->parent = insert_fore;
					new_node->left = NULL;
					new_node->right = NULL;
					
					break;
				}
				else{
					insert_fore = insert_fore->right;
				}
				
			}
			else{
				if(insert_fore->left == NULL){
					new_node = new node;
					new_node->color = red;
					new_node->value = value;
					insert_fore->left = new_node;
					new_node->parent = insert_fore;
					new_node->left = NULL;
					new_node->right = NULL;
					
					break;
				}
				else{
					insert_fore = insert_fore->left;
				}
			}
		}
	}

	insert_case1(new_node);

}

//定义删除树节点函数
void delete_tree(int value){
	node* delete_node = NULL;
	node* save_delete_node = NULL;
	node* save_left_max = NULL;

	delete_node = root;
	//从根开始遍历，找到需要删除的节点
	while(delete_node->value != value){
		if(value > delete_node->value)
			delete_node = delete_node->right;
		else
			delete_node = delete_node->left;
	}
	//保存待删除节点的值
	save_delete_node = delete_node;
	
	//寻找待删除节点左子树的最大值
	save_left_max = delete_node;
	delete_node = delete_node->left;
	//扫描一直到无右孩子为止
	if(delete_node == NULL){
		if(save_delete_node->parent->left == save_delete_node)
			save_delete_node->parent->left = NULL;
		else
			save_delete_node->parent->right = NULL;
		free(save_delete_node);
	}
		
	else{
		while(delete_node->right != NULL){
		delete_node = delete_node->right;
		save_left_max = delete_node;
	}
	/*至此，需要删除的节点M，M左子树的最大值节点P均已找到，P的孩子为N(至多有一个孩子)*/
	/*M为save_delete_node   P为save_left_max*/
	//step1:先用P替换M，颜色不变
	save_delete_node->value = save_left_max->value;
	//step2:如果P有左孩子，使左孩子替换自己的位置，并进行红黑调整
	if(save_left_max->left != NULL){
		save_left_max->color = save_left_max->left->color;
		save_left_max->left = NULL;
		save_left_max->right = NULL;
		save_left_max->value = save_left_max->left->value;
		free(save_left_max->left);
		//调用红黑调整函数
		delete_case1(save_left_max);
	}
	//若P没有左孩子，释放P并直接返回即可
	else{
		free(save_left_max);
		return;
	}
	
	}
	
}

//检查节点颜色并输出
void check_color_out(node* N){
	if(N->color == red){
		SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),FOREGROUND_RED|FOREGROUND_INTENSITY);
		cout<<N->value<<" ";
	}
	else{
		SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),FOREGROUND_BLUE|FOREGROUND_INTENSITY);
		cout<<N->value<<" ";
	}
}

//控制台可视化红黑树
void out_tree(){
	node* start = root;
	node* left = NULL;
	node* right = NULL;
	if(start == root){
		for(int i=num;i>=0;i--)
			cout<<" ";
		if(root->color == black){
			SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),FOREGROUND_BLUE|FOREGROUND_INTENSITY);
			cout<<root->value<<endl;
			left = root->left;
			right = root->right;
		}
		else{
			SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),FOREGROUND_RED|FOREGROUND_INTENSITY);
			cout<<root->value<<endl;
			left = root->left;
			right = root->right;
		}
	}
	//如果输出的不是根节点
	
		for(int i=num-3;i>=0;i++){
			cout<<" ";
		}
		check_color_out(left);
		for(int i=6;i>=1;i--){
			cout<<" ";
		}
		check_color_out(right);
		cout<<endl;
		for(int i=num-6;i>=1;i--){
			cout<<" ";
		}
		check_color_out(left->left);
		for(int i=6;i>=1;i--){
			cout<<" ";
		}
		check_color_out(left->right);
		for(int i=2;i>=1;i--){
			cout<<" ";
		}
		check_color_out(right->left);
		for(int i=6;i>=1;i--){
			cout<<" ";
		}
		check_color_out(right->right);
	


}

//先序遍历输出树的节点(递归)
void pre_order(node* N){
	if(N != NULL){
		check_color_out(N);
		if(N->left != NULL)
			pre_order(N->left);
		if(N->right != NULL)
			pre_order(N->right);
	}
	else
		return ;
}

//查找相关节点函数族
node* uncle(node* N);
node* grandpa(node* N);
node* brother(node* N);

//旋转函数族
void left_rotate(node* N);
void right_rotate(node* N);



int main(){
	
	char choice = 'y';
	int value=0;
	while(choice == 'y'){
		insert();
		cout<<"是否继续插入？(y/n)"<<endl;
		cin>>choice;
	}

	cout<<"请输入要删除的节点:"<<endl;
	cin >> value;
	delete_tree(value);
	cout<<"输出树的前序遍历"<<endl;
	cout<<"*******************"<<endl;
	pre_order(root);
	cout<<endl;
	

	 
}

void left_rotate(node* N){
	node* parent;
	//node* child;
	node* grandfather;
	parent = N->parent;
	grandfather = grandpa(N);

	if(parent == grandfather->left){
		grandfather->left = N;
		
	}
	else{
		grandfather->right = N;
	}
	N->left = parent;
	parent->right = N->left;
}

void right_rotate(node* N){
	node* parent;
	//node* child;
	node* grandfather;
	parent = N->parent;
	grandfather = grandpa(N);

	if(parent == grandfather->left){
		grandfather->left = N;
	}
	else{
		grandfather->right = N;
	}
	N->right = parent;
	parent->left = N->right;
}

//查找brother
node* brother(node* N){
	if(N == N->parent->left)
		return(N->parent->right);
	else
		return(N->parent->left);
}

//查找uncle结点的指针
node* uncle(node* N){
	node* grandpa;
	node* father = NULL;
	grandpa = N->parent->parent;
	father = N->parent;
	if(grandpa->right == father){
		return(grandpa->left);
	}
	else
		return(grandpa->right);
}

//查找grandpa节点
node* grandpa(node* N){
	return(N->parent->parent);
}


void insert_case1(node* N){

	if(N->parent == NULL)
		N->color = black;
	else
		insert_case2(N);
}

void insert_case2(node* N){
	
	if(N->parent->color == black)
		return ;
	else
		insert_case3(N);
}

void insert_case3(node* N){
	
	if(uncle(N) != NULL && uncle(N)->color == red){
		grandpa(N)->color = red;
		N->parent->color = black;
		uncle(N)->color = black;
		insert_case1(grandpa(N));
	}

	else
		insert_case4(N);

}

void insert_case4(node* N){
	//如果N是其父亲F的右孩子并且F是N的祖父G的左孩子，则进行一次左旋操作
	if(N == N->parent->right && N->parent == grandpa(N)->left){
		left_rotate(N);
		N = N->left;
	}
	//如果N是其父亲的左孩子并且其父亲是祖父的右孩子，则进行一次右旋操作
	else if(N == N->left && N->parent == grandpa(N)->right){
		right_rotate(N);
		N = N->right;
	}
	insert_case5(N);
}

void insert_case5(node* N){
	N->parent->color = black;
	grandpa(N)->color = red;
	//如果N是其父亲的左孩子并且N父亲是N祖父的左孩子
	if(N == N->parent->left && N->parent == grandpa(N)->left)
		right_rotate(grandpa(N));
	else
		left_rotate(grandpa(N));

}

void delete_case1(node* N){
	if(N->parent == NULL)
		delete_case2(N);
}

void delete_case2(node* N){
	node* bro;
	bro = brother(N);
	if(bro->color == red){
		N->parent = red;
		bro->color = black;
		if(N == N->parent->left)
			left_rotate(N->parent);
		else
			right_rotate(bro);
	}
	delete_case3(N);
}

void delete_case3(node* N){
	node* bro = brother(N);
	if(N->parent->color == black && bro->color == black &&
		bro->left->color == black && bro->right->color == black)
	{
		bro->color = red;
		delete_case1(N->parent);
	}
	else
		delete_case4(N);
}

void delete_case4(node* N){
	node* bro = brother(N);
	if(bro->color == black && N->parent->color == red && 
		bro->left->color == black && bro->right->color == black)
	{
		bro->color = red;
		N->parent->color = black;
	}
	else
		delete_case5(N);
}

void delete_case5(node* N){
	node* bro;
	bro = brother(N);
	if(bro->color == black){
		if(N == N->parent->left && bro->right->color == black
			&& bro->right->color == red)
		{
			bro->color = red;
			bro->left->color = black;
			right_rotate(bro->left);
		}
		else if(N == N->parent->right && bro->left->color == black 
			&& bro->right->color == red)
		{
			bro->color = red;
			bro->right->color = black;
			left_rotate(bro);
		}	
	}
	delete_case6(N);
}

void delete_case6(node* N){
	node* bro;
	bro = brother(N);

	bro->color = N->parent->color;
	N->parent->color = black;

	if(N == N->parent->left){
		bro->right->color = black;
		left_rotate(N->parent);
	}
	else{
		bro->left->color = black;
		right_rotate(N->parent->left);
	}
}
