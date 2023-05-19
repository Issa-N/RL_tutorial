# RL_tutorial
エラーメッセージ
```
$ git push origin main
To https://github.com/Issa-N/RL_tutorial.git
 ! [rejected]       main -> main (non-fast-forward)
error: failed to push some refs to ‘https://github.com/Issa-N/RL_tutorial.git’
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: ‘git pull ...’) before pushing again.
hint: See the ‘Note about fast-forwards’ in ‘git push --help’ for details.
git pull origin main
git merge origin main
```

1. conflictTest.txtを３人が同時にローカルリポジトリに保存した
2. ３人が別々の内容で編集し、コミットまで行った
3. 1人がpushした後、残りの2人がpushしようとした時に発生した

これは、リモートのブランチで、他の人が更新したファイルと、自分が更新したファイルで競合したことで発生したと考えられる。

$git pull  
$git merge  
を行い、ローカルブランチとリモートブランチと差分を表示させ、それを編集することで解消できた。
